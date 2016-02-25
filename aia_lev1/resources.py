from dataset.resources import BaseMetadataResource
from .models import Metadata


class MetadataResource(BaseMetadataResource):
	
	class Meta(BaseMetadataResource.Meta):
		queryset = Metadata.objects.all()
		resource_name = 'aia_lev1_metadata'
