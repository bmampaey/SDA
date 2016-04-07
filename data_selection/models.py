from __future__ import unicode_literals
from django.db import models

from web_account.models import User
from django.contrib.postgres.fields import ArrayField

from dataset.models import Dataset

class UserDataSelection(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(help_text='Name of the data selection', max_length = 80, null=False, blank=False)
	created = models.DateTimeField(help_text = 'Date of creation', null=False, blank=False, auto_now_add=True)
	updated = models.DateTimeField(help_text = 'Date of last update', null=False, blank=False, auto_now=True)
	
	class Meta:
		ordering = ['-updated']
		get_latest_by = 'updated'
		unique_together = (('user', 'name'),)
		db_table = 'user_data_selection'
		
	def __unicode__(self):
		return u'%s by %s on %s' % (self.name, self.user.username, self.created)
	
	@property
	def number_items(self):
		return sum(data_selection.number_items for data_selection in self.data_selections.all())

	
	@property
	def dataset_names(self):
		return self.data_selections.values_list('dataset', flat=True).distinct()
	

class DataSelection(models.Model):
	user_data_selection = models.ForeignKey(UserDataSelection, related_name = 'data_selections', on_delete=models.CASCADE) # If the UserDataSelection is deleted, delete also the DataSelection
	dataset = models.ForeignKey(Dataset, related_name = 'datasets', related_query_name = 'dataset', on_delete=models.CASCADE)
	query_string = models.TextField(help_text='Query string for the data selection', max_length=2000, null=True, blank=True)
	metadata_oids = ArrayField(models.TextField('Observation ID', help_text = 'Unique identifier for the observation metadata, usually in the form YYYYMMDDHHMMSS'), help_text = 'List of metadata oids', null=True, blank=True)
	created = models.DateTimeField(help_text = 'Date of creation', null=False, blank=False, auto_now_add=True)
	number_items = models.IntegerField(help_text = 'Number of items in the data selection', null=True, blank=True)
	
	class Meta:
		db_table = 'data_selection'
		
	def __unicode__(self):
		return u'%s for %s' % (self.dataset, self.user_data_selection)
	
	def save(self, *args, **kwargs):
		if self.metadata_oids:
			self.number_items = len(self.metadata_oids)
		else:
			self.number_items = self.metadata.count()
		super(DataSelection, self).save(*args, **kwargs)
	
	@property
	def metadata(self):
		if self.metadata_oids:
			return self.dataset.metadata_model.filter(oid__in=self.metadata_oids)
		else:
			query_dict = QueryDict(self.query_string, mutable=True)
			# TODO this is probably wrong and should use the correct resource and use build_filters
			return self.dataset.metadata_model.filter(**query_dict.dict())

