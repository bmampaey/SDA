from __future__ import unicode_literals
from django.db import models
from .base import BaseMetadata

class Themis(BaseMetadata):
	accumul = models.IntegerField('ACCUMUL', help_text='None', blank=True, null=True)
	actifmir = models.NullBooleanField('ACTIFMIR', help_text='None', blank=True, null=True)
	alpha = models.FloatField('ALPHA', help_text='None', blank=True, null=True)
	analys = models.TextField('ANALYS', help_text='None', blank=True, null=True)
	angle = models.IntegerField('ANGLE', help_text='None', blank=True, null=True)
	author = models.TextField('AUTHOR', help_text='None', blank=True, null=True)
	azimuth = models.FloatField('AZIMUTH', help_text='None', blank=True, null=True)
	beamex = models.NullBooleanField('BEAMEX', help_text='None', blank=True, null=True)
	binning = models.TextField('BINNING', help_text='None', blank=True, null=True)
	blank = models.IntegerField('BLANK', help_text='None', blank=True, null=True)
	bscale = models.IntegerField('BSCALE', help_text='None', blank=True, null=True)
	bunit = models.TextField('BUNIT', help_text='None', blank=True, null=True)
	bzero = models.IntegerField('BZERO', help_text='None', blank=True, null=True)
	cam_c = models.IntegerField('CAM_C', help_text='None', blank=True, null=True)
	cam_f = models.IntegerField('CAM_F', help_text='None', blank=True, null=True)
	camhl = models.TextField('CAMHL', help_text='None', blank=True, null=True)
	cmp_desc = models.TextField('CMP_DESC', help_text='None', blank=True, null=True)
	cmp_name = models.TextField('CMP_NAME', help_text='None', blank=True, null=True)
	cmp_no = models.IntegerField('CMP_NO', help_text='None', blank=True, null=True)
	cmp_type = models.TextField('CMP_TYPE', help_text='None', blank=True, null=True)
	colstart = models.IntegerField('COLSTART', help_text='None', blank=True, null=True)
	contact = models.TextField('CONTACT', help_text='None', blank=True, null=True)
	count = models.IntegerField('COUNT', help_text='None', blank=True, null=True)
	ctype1 = models.TextField('CTYPE1', help_text='None', blank=True, null=True)
	ctype2 = models.TextField('CTYPE2', help_text='None', blank=True, null=True)
	ctype3 = models.TextField('CTYPE3', help_text='None', blank=True, null=True)
	date_obs = models.DateTimeField('DATE_OBS', help_text='None', blank=True, null=True)
	delta = models.FloatField('DELTA', help_text='None', blank=True, null=True)
	detector = models.TextField('DETECTOR', help_text='None', blank=True, null=True)
	dimpix = models.TextField('DIMPIX', help_text='None', blank=True, null=True)
	dist_ew = models.FloatField('DIST_EW', help_text='None', blank=True, null=True)
	dist_ns = models.FloatField('DIST_NS', help_text='None', blank=True, null=True)
	eleva = models.FloatField('ELEVA', help_text='None', blank=True, null=True)
	email = models.TextField('EMAIL', help_text='None', blank=True, null=True)
	emgain = models.IntegerField('EMGAIN', help_text='None', blank=True, null=True)
	exptime = models.FloatField('EXPTIME', help_text='None', blank=True, null=True)
	extend = models.NullBooleanField('EXTEND', help_text='None', blank=True, null=True)
	fileacq = models.TextField('FILEACQ', help_text='None', blank=True, null=True)
	filename = models.TextField('FILENAME', help_text='None', blank=True, null=True)
	filterch = models.TextField('FILTERCH', help_text='None', blank=True, null=True)
	filterfe = models.TextField('FILTERFE', help_text='None', blank=True, null=True)
	filtersp = models.TextField('FILTERSP', help_text='None', blank=True, null=True)
	grechel = models.TextField('GRECHEL', help_text='None', blank=True, null=True)
	grpred = models.TextField('GRPRED', help_text='None', blank=True, null=True)
	indlambd = models.IntegerField('INDLAMBD', help_text='None', blank=True, null=True)
	indreg = models.IntegerField('INDREG', help_text='None', blank=True, null=True)
	indstep = models.IntegerField('INDSTEP', help_text='None', blank=True, null=True)
	indstepx = models.IntegerField('INDSTEPX', help_text='None', blank=True, null=True)
	indstepy = models.IntegerField('INDSTEPY', help_text='None', blank=True, null=True)
	institut = models.TextField('INSTITUT', help_text='None', blank=True, null=True)
	instrume = models.TextField('INSTRUME', help_text='None', blank=True, null=True)
	ixwidth = models.IntegerField('IXWIDTH', help_text='None', blank=True, null=True)
	iywidth = models.IntegerField('IYWIDTH', help_text='None', blank=True, null=True)
	latirc = models.FloatField('LATIRC', help_text='None', blank=True, null=True)
	latitud = models.FloatField('LATITUD', help_text='None', blank=True, null=True)
	latstart = models.IntegerField('LATSTART', help_text='None', blank=True, null=True)
	lngstart = models.FloatField('LNGSTART', help_text='None', blank=True, null=True)
	longcarr = models.FloatField('LONGCARR', help_text='None', blank=True, null=True)
	longitud = models.FloatField('LONGITUD', help_text='None', blank=True, null=True)
	longtrc = models.IntegerField('LONGTRC', help_text='None', blank=True, null=True)
	naxis = models.IntegerField('NAXIS', help_text='None', blank=True, null=True)
	naxis1 = models.IntegerField('NAXIS1', help_text='None', blank=True, null=True)
	naxis2 = models.IntegerField('NAXIS2', help_text='None', blank=True, null=True)
	naxis3 = models.IntegerField('NAXIS3', help_text='None', blank=True, null=True)
	nbcam = models.IntegerField('NBCAM', help_text='None', blank=True, null=True)
	nblambd = models.IntegerField('NBLAMBD', help_text='None', blank=True, null=True)
	nbreg = models.IntegerField('NBREG', help_text='None', blank=True, null=True)
	nbstep = models.IntegerField('NBSTEP', help_text='None', blank=True, null=True)
	nbstep_x = models.IntegerField('NBSTEP_X', help_text='None', blank=True, null=True)
	nbstep_y = models.IntegerField('NBSTEP_Y', help_text='None', blank=True, null=True)
	nburst = models.IntegerField('NBURST', help_text='None', blank=True, null=True)
	nbwin = models.IntegerField('NBWIN', help_text='None', blank=True, null=True)
	nobuf = models.IntegerField('NOBUF', help_text='None', blank=True, null=True)
	nocam = models.IntegerField('NOCAM', help_text='None', blank=True, null=True)
	nomask = models.TextField('NOMASK', help_text='None', blank=True, null=True)
	nowin = models.IntegerField('NOWIN', help_text='None', blank=True, null=True)
	nshutter = models.IntegerField('NSHUTTER', help_text='None', blank=True, null=True)
	object = models.TextField('OBJECT', help_text='None', blank=True, null=True)
	obj_id = models.TextField('OBJ_ID', help_text='None', blank=True, null=True)
	observer = models.TextField('OBSERVER', help_text='None', blank=True, null=True)
	obs_mode = models.TextField('OBS_MODE', help_text='None', blank=True, null=True)
	obs_prog = models.TextField('OBS_PROG', help_text='None', blank=True, null=True)
	obs_type = models.TextField('OBS_TYPE', help_text='None', blank=True, null=True)
	offname = models.TextField('OFFNAME', help_text='None', blank=True, null=True)
	offsets = models.NullBooleanField('OFFSETS', help_text='None', blank=True, null=True)
	origin = models.TextField('ORIGIN', help_text='None', blank=True, null=True)
	physpara = models.TextField('PHYSPARA', help_text='None', blank=True, null=True)
	pipeline = models.NullBooleanField('PIPELINE', help_text='None', blank=True, null=True)
	polarang = models.FloatField('POLARANG', help_text='None', blank=True, null=True)
	pol_conf = models.TextField('POL_CONF', help_text='None', blank=True, null=True)
	pol_val = models.TextField('POL_VAL', help_text='None', blank=True, null=True)
	posrot = models.FloatField('POSROT', help_text='None', blank=True, null=True)
	predang = models.IntegerField('PREDANG', help_text='None', blank=True, null=True)
	prefente = models.FloatField('PREFENTE', help_text='None', blank=True, null=True)
	pregain = models.IntegerField('PREGAIN', help_text='None', blank=True, null=True)
	prog_id = models.TextField('PROG_ID', help_text='None', blank=True, null=True)
	prog_num = models.IntegerField('PROG_NUM', help_text='None', blank=True, null=True)
	qwp_name = models.TextField('QWP_NAME', help_text='None', blank=True, null=True)
	rescient = models.TextField('RESCIENT', help_text='None', blank=True, null=True)
	rowstart = models.IntegerField('ROWSTART', help_text='None', blank=True, null=True)
	sci_obj = models.TextField('SCI_OBJ', help_text='None', blank=True, null=True)
	seq_ind = models.IntegerField('SEQ_IND', help_text='None', blank=True, null=True)
	seq_stok = models.TextField('SEQ_STOK', help_text='None', blank=True, null=True)
	solar_b0 = models.FloatField('SOLAR_B0', help_text='None', blank=True, null=True)
	solar_p0 = models.FloatField('SOLAR_P0', help_text='None', blank=True, null=True)
	solar_r = models.FloatField('SOLAR_R', help_text='None', blank=True, null=True)
	solrot_n = models.IntegerField('SOLROT_N', help_text='None', blank=True, null=True)
	spatscal = models.FloatField('SPATSCAL', help_text='None', blank=True, null=True)
	specscal = models.FloatField('SPECSCAL', help_text='None', blank=True, null=True)
	step_x = models.IntegerField('STEP_X', help_text='None', blank=True, null=True)
	step_y = models.IntegerField('STEP_Y', help_text='None', blank=True, null=True)
	svector = models.FloatField('SVECTOR', help_text='None', blank=True, null=True)
	syscoord = models.TextField('SYSCOORD', help_text='None', blank=True, null=True)
	tcycle = models.IntegerField('TCYCLE', help_text='None', blank=True, null=True)
	telescop = models.TextField('TELESCOP', help_text='None', blank=True, null=True)
	tempbmsp = models.IntegerField('TEMPBMSP', help_text='None', blank=True, null=True)
	tempcam = models.IntegerField('TEMPCAM', help_text='None', blank=True, null=True)
	tempqwp1 = models.IntegerField('TEMPQWP1', help_text='None', blank=True, null=True)
	tempqwp2 = models.IntegerField('TEMPQWP2', help_text='None', blank=True, null=True)
	themisff = models.IntegerField('THEMISFF', help_text='None', blank=True, null=True)
	timestep = models.IntegerField('TIMESTEP', help_text='None', blank=True, null=True)
	tregion = models.IntegerField('TREGION', help_text='None', blank=True, null=True)
	wavelnth = models.IntegerField('WAVELNTH', help_text='None', blank=True, null=True)
	waveunit = models.IntegerField('WAVEUNIT', help_text='None', blank=True, null=True)
	yfirst = models.NullBooleanField('YFIRST', help_text='None', blank=True, null=True)
