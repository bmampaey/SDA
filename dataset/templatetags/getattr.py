# From https://snipt.net/Fotinakis/django-template-tag-for-dynamic-attribute-lookups/

# To use, in template:
# {% load getattr %}
# {{ object|getattr:dynamic_string_var }}

import re
from django import template
from django.conf import settings

numeric_test = re.compile("^\d+$")
register = template.Library()

def getattribute(value, arg):
	"""Gets an attribute of an object dynamically from a string name"""

	if hasattr(value, str(arg)):
		return getattr(value, arg)
	elif hasattr(value, 'has_key') and value.has_key(arg):
		return value[arg]
	elif numeric_test.match(str(arg)) and len(value) > int(arg):
		return value[int(arg)]
	else:
		return settings.TEMPLATE_STRING_IF_INVALID

register.filter('getattr', getattribute)
