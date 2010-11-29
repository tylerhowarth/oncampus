import os
import re

from google.appengine.api import urlfetch
import urllib
from django.utils.html import escape

from google.appengine.ext import db
from django.utils import simplejson

class Event(db.Model):
	title = db.StringProperty()
	location = db.StringProperty()
	description = db.StringProperty()
	time = db.StringProperty()
	
	tag = db.StringProperty()
	
	short_url = db.StringProperty()
	qr_code = db.StringProperty()
	
	created_at = db.DateTimeProperty(auto_now_add=True)
	
	
	# def upload(self, offset):
	# 	courses = simplejson.loads(str(self.content))
	# 	
	# 	if int(offset) == 0:
	# 		delete = "http://engineering.colorado.edu/nebula/?v=admin/delete_all&password=letmein"
	# 		urlfetch.fetch(delete)
	# 	
	# 	# print "<html><body>"
	# 	count = 10
	# 	offset = int(offset)
	# 	for c in courses[(offset*count):(offset*count)+count]:
	# 		save = "http://engineering.colorado.edu/homersearch/?v=admin/save&%s"
	# 		# print " ".join([c['number'], escape(c['title'].replace("'", "", 10)).replace("'", "", 10)])
	# 		params = urllib.urlencode({'number': c['number'], 'title': c['title'].replace("'", "").replace("\"", ""), 'tag_list': c['tags']})
	# 		response = urlfetch.fetch(save % params)
	# 		# print "<br/><small>" + response.content + "</small>"
	# 		# print "<br/><br/>"
	# 	
	# 	return len(courses[(offset*count):(offset*count)+count])
	# 	
	# 	# print "<a href='/admin/'>Back to admin</a>"
	# 	
	# @staticmethod
	# def current():
	# 	try:
	# 		return CourseList.all().order('-created_at').fetch(1).pop()
	# 	except Exception:
	# 		db.put(CourseList(content="[]"))
	# 		return CourseList.all().order('-created_at').fetch(1).pop()
