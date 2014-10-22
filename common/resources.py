from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS, url
from tastypie.authorization import DjangoAuthorization
from tastypie.utils import trailing_slash
from taggit.models import Tag

from common.tastypie_paginator import EstimatedCountPaginator

class TagResource(ModelResource):
	class Meta:
		queryset = Tag.objects.all()

class BaseResource(ModelResource):
	"""Base class to set common parameters to all resources"""
	class Meta:
		limit = 20
		#include_absolute_url = True
		paginator_class = EstimatedCountPaginator
		authorization = DjangoAuthorization()
	
#	def base_urls(self):
#		"""
#		The standard URLs this ``Resource`` should respond to.
#		"""
#		# Due to the way Django parses URLs, ``get_multiple`` won't work without
#		# a trailing slash.
#		return [
#			url(r"^%s/(?P<resource_name>%s)%s$" % (self.dataset_name, self._meta.resource_type, trailing_slash()), self.wrap_view('dispatch_list'), name="api_dispatch_list"),
#			url(r"^%s/(?P<resource_name>%s)/schema%s$" % (self.dataset_name, self._meta.resource_type, trailing_slash()), self.wrap_view('get_schema'), name="api_get_schema"),
#			url(r"^%s/(?P<resource_name>%s)/set/(?P<pk_list>\w[\w/;-]*)/$" % (self.dataset_name, self._meta.resource_type), self.wrap_view('get_multiple'), name="api_get_multiple"),
#			url(r"^%s/(?P<resource_name>%s)/(?P<pk>\w[\w/-]*)%s$" % (self.dataset_name, self._meta.resource_type, trailing_slash()), self.wrap_view('dispatch_detail'), name="api_dispatch_detail"),
#		]

def KeywordResource_for(dataset_name, Keyword):
	"""Create a KeywordResource class for a specific dataset"""
	
	class KeywordResource(BaseResource):
		
		class Meta(BaseResource.Meta):
			queryset = Keyword.objects.all()
			resource_name = dataset_name + '_keyword'
			resource_type = 'keyword'
	
		def __init__(self, *args, **kwargs):
			self.dataset_name = dataset_name
			self._meta.paginator_class.setup(connection_name = self.dataset_name)
			super(KeywordResource, self).__init__(*args, **kwargs)
	
	return KeywordResource


def DataLocationResource_for(dataset_name, DataLocation):
	"""Create a DataLocationResource class for a specific dataset"""
	
	class DataLocationResource(BaseResource):
		meta_data = fields.OneToOneField(dataset_name+'.resources.MetaDataResource', 'meta_data', related_name='data_location', null=True, blank=True)
	
		class Meta(BaseResource.Meta):
			queryset = DataLocation.objects.all()
			resource_name = dataset_name + '_data_location'
			resource_type = 'data_location'
	
		def __init__(self, *args, **kwargs):
			self.dataset_name = dataset_name
			self._meta.paginator_class.setup(connection_name = self.dataset_name)
			super(DataLocationResource, self).__init__(*args, **kwargs)
	
	return DataLocationResource


def MetaDataResource_for(dataset_name, MetaData):
	"""Create a MetaDataResource class for a specific dataset"""
	
	class MetaDataResource(BaseResource):
		data_location = fields.OneToOneField(dataset_name+'.resources.DataLocationResource', 'data_location', related_name='meta_data', full=True, null=True, blank=True)
		tags = fields.ToManyField(TagResource, 'tags', full=True)
		class Meta(BaseResource.Meta):
			queryset = MetaData.objects.all()
			resource_name = dataset_name + '_meta_data'
			resource_type = 'meta_data'
	
		def __init__(self, *args, **kwargs):
			self.dataset_name = dataset_name
			self._meta.paginator_class.setup(connection_name = self.dataset_name)
			super(MetaDataResource, self).__init__(*args, **kwargs)
	
	return MetaDataResource