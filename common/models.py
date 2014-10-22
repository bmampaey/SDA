from django.db import models

class BaseMetaData(models.Model):
	id = models.BigIntegerField(primary_key=True)
	tags = models.ManyToManyField('Tag', related_name = "%(app_label)s_%(class)s")
	
	class Meta:
		abstract = True
		db_table = 'meta_data'
	
	def __unicode__(self):
		return unicode(self.id)
	
	@property
	def tags_names(self):
		return self.tags.values_list('name', flat=True)

class BaseKeyword(models.Model):
	PYTHON_TYPE_CHOICES = (
		("str", "string"),
		("bool", "bool"),
		("int", "int"),
		("float", "float"),
		("datetime", "datetime (iso format)"),
	)
	db_column = models.TextField("Column name of the corresponding keyword in the meta_data table.", max_length=30, primary_key = True)
	name = models.CharField(help_text = "Fits like name of the keyword. Can contain space and dashes.", blank=True, null=True, max_length=70)
	python_type = models.CharField(help_text = "Python type of the keyword.", blank=True, null=False, max_length=12, default = "string", choices = PYTHON_TYPE_CHOICES)
	unit = models.CharField(help_text = "Physical unit (SI compliant) of the keyword.", blank=True, null=True, max_length=10)
	description = models.TextField(help_text = "Full description of the keyword.", blank=True, null=True, max_length=70)
	
	class Meta:
		abstract = True
		db_table = "keyword"
	
	def __unicode__(self):
		return unicode(self.name)
	
	@classmethod
	def number_tagged(cls, tags):
		cls.objects.filter(tags__in=tags).count()


class BaseDataLocation(models.Model):
	
	url = models.TextField(help_text = "URL of the data at the data site.", max_length=255, blank=True, null=True)
	
	class Meta:
		abstract = True
		db_table = "data_location"
	
	def __unicode__(self):
		return unicode(self.url)

class BaseTag(models.Model):
	name = models.TextField(primary_key=True, blank=False, null=False)
	
	class Meta:
		abstract = True
		db_table = "tag"
	
	def __unicode__(self):
		return unicode(self.name)
	
	@classmethod
	def all_tags(cls):
		tags = [sub_model.objects.values_list("name", flat=True) for sub_model in cls.__subclasses__()]
		return set([t for ts in tags for t in ts])