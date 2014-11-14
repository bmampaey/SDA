from collections import OrderedDict

from common.views import BaseSearchDataForm, BaseSearchDataResults, BaseDownloadData
from hmi_magnetogram.forms import SearchData
from hmi_magnetogram.models import MetaData, DataLocation

class SearchDataForm(BaseSearchDataForm):
	dataset_name = "hmi_magnetogram"
	search_form_class = SearchData

class SearchDataResults(BaseSearchDataResults):
	dataset_name = "hmi_magnetogram"
	model = MetaData
	search_form_class = SearchData
	table_columns = OrderedDict([("date_obs", "Date Observation"), ("quality", "Quality")])

class DownloadData(BaseDownloadData):
	data_location_model = DataLocation
