from datetime import datetime
from dateutil.parser import parse as parse_date
from importlib import import_module
from django.core.management.base import BaseCommand, CommandError
from ..logger import Logger

class Command(BaseCommand):
	help = 'Populate the Metadata and DataLocation for a dataset'
	
	def add_arguments(self, parser):
		parser.add_argument('dataset', help='The id of the dataset.')
		parser.add_argument('start_date', type = lambda s: parse_date(s), help='The start date.')
		parser.add_argument('end_date', nargs = '?', type = lambda s: parse_date(s), default = datetime.utcnow(), help='The end date.')
		parser.add_argument('--update', default = False, action='store_true', help='Update metadata even if already present in DB')
		
	def handle(self, **options):
		# Create a populator for the dataset
		try:
			populate = ('metadata.management.records' + options['dataset'])
			populator = populate.Populator(Logger(self))
		except Exception, why:
			raise CommandError('Cannot create a populator for dataset %s: %s' % (options['dataset'], why))
		
		# Run the populator
		populator.run(options['start_date'], options['end_date'], options['update'])