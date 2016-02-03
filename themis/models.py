from __future__ import unicode_literals
from django.db import models
from common.models import BaseMetadata

class Metadata(BaseMetadata):
	rowstart = models.IntegerField(blank=True, null=True)
	fileacq = models.TextField(blank=True, null=True)
	nblambd = models.IntegerField(blank=True, null=True)
	nowin = models.IntegerField(blank=True, null=True)
	grechel = models.TextField(blank=True, null=True)
	filtersp = models.TextField(blank=True, null=True)
	waveunit = models.IntegerField(blank=True, null=True)
	filterch = models.TextField(blank=True, null=True)
	step_y = models.IntegerField(blank=True, null=True)
	step_x = models.IntegerField(blank=True, null=True)
	posrot = models.FloatField(blank=True, null=True)
	eleva = models.FloatField(blank=True, null=True)
	predang = models.IntegerField(blank=True, null=True)
	timestep = models.IntegerField(blank=True, null=True)
	lngstart = models.FloatField(blank=True, null=True)
	analys = models.TextField(blank=True, null=True)
	solar_r = models.FloatField(blank=True, null=True)
	seq_ind = models.IntegerField(blank=True, null=True)
	iywidth = models.IntegerField(blank=True, null=True)
	nbreg = models.IntegerField(blank=True, null=True)
	dist_ew = models.FloatField(blank=True, null=True)
	prog_id = models.TextField(blank=True, null=True)
	exptime = models.FloatField(blank=True, null=True)
	nbwin = models.IntegerField(blank=True, null=True)
	bunit = models.TextField(blank=True, null=True)
	bscale = models.IntegerField(blank=True, null=True)
	telescop = models.TextField(blank=True, null=True)
	specscal = models.FloatField(blank=True, null=True)
	observer = models.TextField(blank=True, null=True)
	ctype3 = models.TextField(blank=True, null=True)
	offname = models.TextField(blank=True, null=True)
	ctype1 = models.TextField(blank=True, null=True)
	tregion = models.IntegerField(blank=True, null=True)
	ctype2 = models.TextField(blank=True, null=True)
	indstepy = models.IntegerField(blank=True, null=True)
	indstepx = models.IntegerField(blank=True, null=True)
	dist_ns = models.FloatField(blank=True, null=True)
	filename = models.TextField(blank=True, null=True)
	nbcam = models.IntegerField(blank=True, null=True)
	email = models.TextField(blank=True, null=True)
	obs_type = models.TextField(blank=True, null=True)
	longtrc = models.IntegerField(blank=True, null=True)
	extend = models.NullBooleanField(blank=True, null=True)
	offsets = models.NullBooleanField(blank=True, null=True)
	solar_b0 = models.FloatField(blank=True, null=True)
	nshutter = models.IntegerField(blank=True, null=True)
	nburst = models.IntegerField(blank=True, null=True)
	institut = models.TextField(blank=True, null=True)
	pipeline = models.NullBooleanField(blank=True, null=True)
	seq_stok = models.TextField(blank=True, null=True)
	wavelnth = models.IntegerField(blank=True, null=True)
	solar_p0 = models.FloatField(blank=True, null=True)
	tcycle = models.IntegerField(blank=True, null=True)
	yfirst = models.NullBooleanField(blank=True, null=True)
	author = models.TextField(blank=True, null=True)
	tempbmsp = models.IntegerField(blank=True, null=True)
	bzero = models.IntegerField(blank=True, null=True)
	physpara = models.TextField(blank=True, null=True)
	prog_num = models.IntegerField(blank=True, null=True)
	pol_val = models.TextField(blank=True, null=True)
	nobuf = models.IntegerField(blank=True, null=True)
	blank = models.IntegerField(blank=True, null=True)
	colstart = models.IntegerField(blank=True, null=True)
	tempcam = models.IntegerField(blank=True, null=True)
	cam_f = models.IntegerField(blank=True, null=True)
	cmp_no = models.IntegerField(blank=True, null=True)
	cam_c = models.IntegerField(blank=True, null=True)
	naxis1 = models.IntegerField(blank=True, null=True)
	naxis3 = models.IntegerField(blank=True, null=True)
	naxis2 = models.IntegerField(blank=True, null=True)
	cmp_desc = models.TextField(blank=True, null=True)
	accumul = models.IntegerField(blank=True, null=True)
	solrot_n = models.IntegerField(blank=True, null=True)
	svector = models.FloatField(blank=True, null=True)
	nomask = models.TextField(blank=True, null=True)
	indreg = models.IntegerField(blank=True, null=True)
	actifmir = models.NullBooleanField(blank=True, null=True)
	binning = models.TextField(blank=True, null=True)
	spatscal = models.FloatField(blank=True, null=True)
	polarang = models.FloatField(blank=True, null=True)
	indstep = models.IntegerField(blank=True, null=True)
	delta = models.FloatField(blank=True, null=True)
	origin = models.TextField(blank=True, null=True)
	count = models.IntegerField(blank=True, null=True)
	filterfe = models.TextField(blank=True, null=True)
	date_obs = models.DateTimeField(blank=True, null=True)
	rescient = models.TextField(blank=True, null=True)
	latirc = models.FloatField(blank=True, null=True)
	syscoord = models.TextField(blank=True, null=True)
	grpred = models.TextField(blank=True, null=True)
	obj_id = models.TextField(blank=True, null=True)
	sci_obj = models.TextField(blank=True, null=True)
	dimpix = models.TextField(blank=True, null=True)
	latitud = models.FloatField(blank=True, null=True)
	cmp_name = models.TextField(blank=True, null=True)
	tempqwp2 = models.IntegerField(blank=True, null=True)
	obs_prog = models.TextField(blank=True, null=True)
	tempqwp1 = models.IntegerField(blank=True, null=True)
	pol_conf = models.TextField(blank=True, null=True)
	latstart = models.IntegerField(blank=True, null=True)
	nbstep_y = models.IntegerField(blank=True, null=True)
	nbstep_x = models.IntegerField(blank=True, null=True)
	naxis = models.IntegerField(blank=True, null=True)
	angle = models.IntegerField(blank=True, null=True)
	nocam = models.IntegerField(blank=True, null=True)
	obs_mode = models.TextField(blank=True, null=True)
	instrume = models.TextField(blank=True, null=True)
	qwp_name = models.TextField(blank=True, null=True)
	nbstep = models.IntegerField(blank=True, null=True)
	detector = models.TextField(blank=True, null=True)
	ixwidth = models.IntegerField(blank=True, null=True)
	longcarr = models.FloatField(blank=True, null=True)
	object = models.TextField(blank=True, null=True)
	camhl = models.TextField(blank=True, null=True)
	themisff = models.IntegerField(blank=True, null=True)
	prefente = models.FloatField(blank=True, null=True)
	alpha = models.FloatField(blank=True, null=True)
	longitud = models.FloatField(blank=True, null=True)
	indlambd = models.IntegerField(blank=True, null=True)
	emgain = models.IntegerField(blank=True, null=True)
	pregain = models.IntegerField(blank=True, null=True)
	cmp_type = models.TextField(blank=True, null=True)
	beamex = models.NullBooleanField(blank=True, null=True)
	contact = models.TextField(blank=True, null=True)
	azimuth = models.FloatField(blank=True, null=True)
