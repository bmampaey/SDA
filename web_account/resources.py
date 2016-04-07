from django.conf.urls import url
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError

from tastypie.http import HttpUnauthorized, HttpForbidden
from tastypie.resources import ModelResource
from tastypie.utils import trailing_slash

from web_account.models import User


class UserResource(ModelResource):
	'''Allow to login or logout a user from email only. On login create user if it does not exists.'''
	class Meta:
		queryset = User.objects.all()
		fields = []
		allowed_methods = ['get', 'post']
		resource_name = 'user'
		list_allowed_methods = []
		detail_allowed_methods = []
	
	def prepend_urls(self):
		return [
			url(r"^(?P<resource_name>%s)/login%s$" % (self._meta.resource_name, trailing_slash), self.wrap_view('login'), name="api_login"),
			url(r'^(?P<resource_name>%s)/logout%s$' % (self._meta.resource_name, trailing_slash), self.wrap_view('logout'), name='api_logout'),
		]
	
	def login(self, request, **kwargs):
		self.method_check(request, allowed=['post'])
		
		# Extract the email from the request data
		data = self.deserialize(request, request.body)
		email = data.get('email', '')
		
		# We extract the username from the email
		username, _ = email.split('@', 1)
		
		# If the user does not exists we create it
		user, created = User.objects.get_or_create(email = email, defaults = {'username' : username})
		
		# Check that user is active and login is successfull
		if user.is_active and user.do_login():
			return self.create_response(request, {'username': user.username, 'api_key': user.api_key})
		else:
			return self.create_response(request, 'Your account is disabled. Please contact the site administrators for help.', HttpForbidden)
	
	def logout(self, request, **kwargs):
		self.method_check(request, allowed=['get'])
		if request.user and request.user.is_authenticated():
			return self.create_response(request, {'success': True})
		else:
			return self.create_response(request, {'success': False}, HttpUnauthorized)