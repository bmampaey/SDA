from SDA.authorizations import AlwaysReadAuthorization
from SDA.authentication import AuthUserApiKeyAuthentication
from SDA.serializers import Serializer
from tastypie.cache import SimpleCache

class ResourceMeta:
	'''Base class to set common parameters to all resources'''
	max_limit = 100
	authentication = AuthUserApiKeyAuthentication()
	authorization = AlwaysReadAuthorization()
	serializer = Serializer()
	# Necessary for tastypie angular resource
	always_return_data = True
	# Cache for a long time
	cache = SimpleCache(timeout=60 * 60 * 24)

