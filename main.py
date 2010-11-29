#!/usr/bin/env python
#
# Copyright 2010 Ben Jacobson Enterprisezzz
#

import os
import re

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
from google.appengine.api import urlfetch
from django.utils import simplejson as json

from domain import *


class BaseHandler(webapp.RequestHandler):
	def render(self, template_name, args={}):
		path = os.path.join(os.path.dirname(__file__), 'templates/' + template_name)
		self.response.out.write(webapp.template.render(path, args))


class MainHandler(BaseHandler):
	def get(self):
		self.render("index.html")


class EventHandler(BaseHandler):
	def get(self):
		self.render('event.html')


class AdminHandler(BaseHandler):
	def get(self):
		events = Event.all().order("tag").fetch(20)
		if(len(events) == 0):
			events = []
		self.render('admin/home.html', {"events":events})
	def post(self):
		event = Event()
		for k in ['title', 'description', 'location', 'time', 'tag']:
			setattr(event, k, self.request.get(k))
		db.put(event)
		
		form_fields = { "url": "http://oncampus-project.appspot.com/event?key=" + str(event.key) }
		form_data = urllib.urlencode(form_fields)
		result = urlfetch.fetch(url="http://goo.gl/api/shorten",
								payload=form_data,
								method=urlfetch.POST)
								
		if result.status_code >= 200 and result.status_code <= 210:
			res = json.loads(result.content)
			print res
			print ['short_url']
			event.short_url = res['short_url']
			event.qr_code = res['short_url'] + ".qr"
			db.put(event)
		
		self.redirect('/admin')

class DeleteHandler(BaseHandler):
	def get(self):
		event = db.get(self.request.get("key"))
		db.delete(event)
		self.redirect('/admin')

def main():
	application = webapp.WSGIApplication([
		('/', MainHandler),
		('/event', EventHandler),
		('/admin', AdminHandler),
		('/admin/delete', DeleteHandler),
	],debug=True)
	util.run_wsgi_app(application)

if __name__ == '__main__':
	main()









