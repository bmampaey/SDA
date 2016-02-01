from __future__ import unicode_literals

from common.models import BaseMetadata

class Metadata(BaseMetadata):
	bld_vers = models.TextField(help_text='BLD_VERS', blank=True)
	lvl_num = models.FloatField(help_text='LVL_NUM', blank=True, null=True)
	t_rec = models.DateTimeField(help_text='T_REC', blank=True, null=True)
	origin = models.TextField(help_text='ORIGIN', blank=True)
	date = models.DateTimeField(help_text='DATE', blank=True, null=True)
	telescop = models.TextField(help_text='TELESCOP', blank=True)
	instrume = models.TextField(help_text='INSTRUME', blank=True)
	date_obs = models.DateTimeField(help_text='DATE-OBS', blank=True, null=True)
	t_obs = models.DateTimeField(help_text='T_OBS', blank=True, null=True)
	camera = models.IntegerField(help_text='CAMERA', blank=True, null=True)
	img_type = models.TextField(help_text='IMG_TYPE', blank=True)
	exptime = models.FloatField(help_text='EXPTIME', blank=True, null=True)
	expsdev = models.FloatField(help_text='EXPSDEV', blank=True, null=True)
	int_time = models.FloatField(help_text='INT_TIME', blank=True, null=True)
	wavelnth = models.IntegerField(help_text='WAVELNTH', blank=True, null=True)
	waveunit = models.TextField(help_text='WAVEUNIT', blank=True)
	wave_str = models.TextField(help_text='WAVE_STR', blank=True)
	fsn = models.IntegerField(help_text='FSN', blank=True, null=True)
	fid = models.IntegerField(help_text='FID', blank=True, null=True)
	quallev0 = models.IntegerField(help_text='QUALLEV0', blank=True, null=True)
	quality = models.IntegerField(help_text='QUALITY', blank=True, null=True)
	totvals = models.IntegerField(help_text='TOTVALS', blank=True, null=True)
	datavals = models.IntegerField(help_text='DATAVALS', blank=True, null=True)
	missvals = models.IntegerField(help_text='MISSVALS', blank=True, null=True)
	percentd = models.FloatField(help_text='PERCENTD', blank=True, null=True)
	datamin = models.IntegerField(help_text='DATAMIN', blank=True, null=True)
	datamax = models.IntegerField(help_text='DATAMAX', blank=True, null=True)
	datamedn = models.IntegerField(help_text='DATAMEDN', blank=True, null=True)
	datamean = models.FloatField(help_text='DATAMEAN', blank=True, null=True)
	datarms = models.FloatField(help_text='DATARMS', blank=True, null=True)
	dataskew = models.FloatField(help_text='DATASKEW', blank=True, null=True)
	datakurt = models.FloatField(help_text='DATAKURT', blank=True, null=True)
	datacent = models.FloatField(help_text='DATACENT', blank=True, null=True)
	datap01 = models.FloatField(help_text='DATAP01', blank=True, null=True)
	datap10 = models.FloatField(help_text='DATAP10', blank=True, null=True)
	datap25 = models.FloatField(help_text='DATAP25', blank=True, null=True)
	datap75 = models.FloatField(help_text='DATAP75', blank=True, null=True)
	datap90 = models.FloatField(help_text='DATAP90', blank=True, null=True)
	datap95 = models.FloatField(help_text='DATAP95', blank=True, null=True)
	datap98 = models.FloatField(help_text='DATAP98', blank=True, null=True)
	datap99 = models.FloatField(help_text='DATAP99', blank=True, null=True)
	nsatpix = models.IntegerField(help_text='NSATPIX', blank=True, null=True)
	oscnmean = models.FloatField(help_text='OSCNMEAN', blank=True, null=True)
	oscnrms = models.FloatField(help_text='OSCNRMS', blank=True, null=True)
	flat_rec = models.TextField(help_text='FLAT_REC', blank=True)
	nspikes = models.IntegerField(help_text='NSPIKES', blank=True, null=True)
	ctype1 = models.TextField(help_text='CTYPE1', blank=True)
	cunit1 = models.TextField(help_text='CUNIT1', blank=True)
	crval1 = models.FloatField(help_text='CRVAL1', blank=True, null=True)
	cdelt1 = models.FloatField(help_text='CDELT1', blank=True, null=True)
	crpix1 = models.FloatField(help_text='CRPIX1', blank=True, null=True)
	ctype2 = models.TextField(help_text='CTYPE2', blank=True)
	cunit2 = models.TextField(help_text='CUNIT2', blank=True)
	crval2 = models.FloatField(help_text='CRVAL2', blank=True, null=True)
	cdelt2 = models.FloatField(help_text='CDELT2', blank=True, null=True)
	crpix2 = models.FloatField(help_text='CRPIX2', blank=True, null=True)
	crota2 = models.FloatField(help_text='CROTA2', blank=True, null=True)
	r_sun = models.FloatField(help_text='R_SUN', blank=True, null=True)
	mpo_rec = models.TextField(help_text='MPO_REC', blank=True)
	inst_rot = models.FloatField(help_text='INST_ROT', blank=True, null=True)
	imscl_mp = models.FloatField(help_text='IMSCL_MP', blank=True, null=True)
	x0_mp = models.FloatField(help_text='X0_MP', blank=True, null=True)
	y0_mp = models.FloatField(help_text='Y0_MP', blank=True, null=True)
	asd_rec = models.TextField(help_text='ASD_REC', blank=True)
	sat_y0 = models.FloatField(help_text='SAT_Y0', blank=True, null=True)
	sat_z0 = models.FloatField(help_text='SAT_Z0', blank=True, null=True)
	sat_rot = models.FloatField(help_text='SAT_ROT', blank=True, null=True)
	acs_mode = models.TextField(help_text='ACS_MODE', blank=True)
	acs_eclp = models.TextField(help_text='ACS_ECLP', blank=True)
	acs_sunp = models.TextField(help_text='ACS_SUNP', blank=True)
	acs_safe = models.TextField(help_text='ACS_SAFE', blank=True)
	acs_cgt = models.TextField(help_text='ACS_CGT', blank=True)
	orb_rec = models.TextField(help_text='ORB_REC', blank=True)
	dsun_ref = models.FloatField(help_text='DSUN_REF', blank=True, null=True)
	dsun_obs = models.FloatField(help_text='DSUN_OBS', blank=True, null=True)
	rsun_ref = models.FloatField(help_text='RSUN_REF', blank=True, null=True)
	rsun_obs = models.FloatField(help_text='RSUN_OBS', blank=True, null=True)
	gaex_obs = models.FloatField(help_text='GAEX_OBS', blank=True, null=True)
	gaey_obs = models.FloatField(help_text='GAEY_OBS', blank=True, null=True)
	gaez_obs = models.FloatField(help_text='GAEZ_OBS', blank=True, null=True)
	haex_obs = models.FloatField(help_text='HAEX_OBS', blank=True, null=True)
	haey_obs = models.FloatField(help_text='HAEY_OBS', blank=True, null=True)
	haez_obs = models.FloatField(help_text='HAEZ_OBS', blank=True, null=True)
	obs_vr = models.FloatField(help_text='OBS_VR', blank=True, null=True)
	obs_vw = models.FloatField(help_text='OBS_VW', blank=True, null=True)
	obs_vn = models.FloatField(help_text='OBS_VN', blank=True, null=True)
	crln_obs = models.FloatField(help_text='CRLN_OBS', blank=True, null=True)
	crlt_obs = models.FloatField(help_text='CRLT_OBS', blank=True, null=True)
	car_rot = models.IntegerField(help_text='CAR_ROT', blank=True, null=True)
	hgln_obs = models.FloatField(help_text='HGLN_OBS', blank=True, null=True)
	hglt_obs = models.FloatField(help_text='HGLT_OBS', blank=True, null=True)
	roi_nwin = models.IntegerField(help_text='ROI_NWIN', blank=True, null=True)
	roi_sum = models.IntegerField(help_text='ROI_SUM', blank=True, null=True)
	roi_nax1 = models.IntegerField(help_text='ROI_NAX1', blank=True, null=True)
	roi_nay1 = models.IntegerField(help_text='ROI_NAY1', blank=True, null=True)
	roi_llx1 = models.IntegerField(help_text='ROI_LLX1', blank=True, null=True)
	roi_lly1 = models.IntegerField(help_text='ROI_LLY1', blank=True, null=True)
	roi_nax2 = models.IntegerField(help_text='ROI_NAX2', blank=True, null=True)
	roi_nay2 = models.IntegerField(help_text='ROI_NAY2', blank=True, null=True)
	roi_llx2 = models.IntegerField(help_text='ROI_LLX2', blank=True, null=True)
	roi_lly2 = models.IntegerField(help_text='ROI_LLY2', blank=True, null=True)
	pixlunit = models.TextField(help_text='PIXLUNIT', blank=True)
	dn_gain = models.FloatField(help_text='DN_GAIN', blank=True, null=True)
	eff_area = models.FloatField(help_text='EFF_AREA', blank=True, null=True)
	eff_ar_v = models.FloatField(help_text='EFF_AR_V', blank=True, null=True)
	tempccd = models.FloatField(help_text='TEMPCCD', blank=True, null=True)
	tempgt = models.FloatField(help_text='TEMPGT', blank=True, null=True)
	tempsmir = models.FloatField(help_text='TEMPSMIR', blank=True, null=True)
	tempfpad = models.FloatField(help_text='TEMPFPAD', blank=True, null=True)
	ispsname = models.TextField(help_text='ISPSNAME', blank=True)
	isppktim = models.DateTimeField(help_text='ISPPKTIM', blank=True, null=True)
	isppktvn = models.TextField(help_text='ISPPKTVN', blank=True)
	aivnmst = models.IntegerField(help_text='AIVNMST', blank=True, null=True)
	aimgots = models.IntegerField(help_text='AIMGOTS', blank=True, null=True)
	asqhdr = models.BigIntegerField(help_text='ASQHDR', blank=True, null=True)
	asqtnum = models.SmallIntegerField(help_text='ASQTNUM', blank=True, null=True)
	asqfsn = models.IntegerField(help_text='ASQFSN', blank=True, null=True)
	aiahfsn = models.IntegerField(help_text='AIAHFSN', blank=True, null=True)
	aecdelay = models.IntegerField(help_text='AECDELAY', blank=True, null=True)
	aiaecti = models.IntegerField(help_text='AIAECTI', blank=True, null=True)
	aiasen = models.IntegerField(help_text='AIASEN', blank=True, null=True)
	aifdbid = models.IntegerField(help_text='AIFDBID', blank=True, null=True)
	aimgotss = models.IntegerField(help_text='AIMGOTSS', blank=True, null=True)
	aifcps = models.SmallIntegerField(help_text='AIFCPS', blank=True, null=True)
	aiftswth = models.IntegerField(help_text='AIFTSWTH', blank=True, null=True)
	aifrmlid = models.IntegerField(help_text='AIFRMLID', blank=True, null=True)
	aiftsid = models.IntegerField(help_text='AIFTSID', blank=True, null=True)
	aihismxb = models.IntegerField(help_text='AIHISMXB', blank=True, null=True)
	aihis192 = models.IntegerField(help_text='AIHIS192', blank=True, null=True)
	aihis348 = models.IntegerField(help_text='AIHIS348', blank=True, null=True)
	aihis604 = models.IntegerField(help_text='AIHIS604', blank=True, null=True)
	aihis860 = models.IntegerField(help_text='AIHIS860', blank=True, null=True)
	aifwen = models.IntegerField(help_text='AIFWEN', blank=True, null=True)
	aimgshce = models.IntegerField(help_text='AIMGSHCE', blank=True, null=True)
	aectype = models.SmallIntegerField(help_text='AECTYPE', blank=True, null=True)
	aecmode = models.TextField(help_text='AECMODE', blank=True)
	aistate = models.TextField(help_text='AISTATE', blank=True)
	aiaecenf = models.SmallIntegerField(help_text='AIAECENF', blank=True, null=True)
	aifiltyp = models.SmallIntegerField(help_text='AIFILTYP', blank=True, null=True)
	aimshobc = models.FloatField(help_text='AIMSHOBC', blank=True, null=True)
	aimshobe = models.FloatField(help_text='AIMSHOBE', blank=True, null=True)
	aimshotc = models.FloatField(help_text='AIMSHOTC', blank=True, null=True)
	aimshote = models.FloatField(help_text='AIMSHOTE', blank=True, null=True)
	aimshcbc = models.FloatField(help_text='AIMSHCBC', blank=True, null=True)
	aimshcbe = models.FloatField(help_text='AIMSHCBE', blank=True, null=True)
	aimshctc = models.FloatField(help_text='AIMSHCTC', blank=True, null=True)
	aimshcte = models.FloatField(help_text='AIMSHCTE', blank=True, null=True)
	aicfgdl1 = models.SmallIntegerField(help_text='AICFGDL1', blank=True, null=True)
	aicfgdl2 = models.SmallIntegerField(help_text='AICFGDL2', blank=True, null=True)
	aicfgdl3 = models.SmallIntegerField(help_text='AICFGDL3', blank=True, null=True)
	aicfgdl4 = models.SmallIntegerField(help_text='AICFGDL4', blank=True, null=True)
	aifoenfl = models.SmallIntegerField(help_text='AIFOENFL', blank=True, null=True)
	aimgfsn = models.IntegerField(help_text='AIMGFSN', blank=True, null=True)
	aimgtyp = models.IntegerField(help_text='AIMGTYP', blank=True, null=True)
	aiawvlen = models.IntegerField(help_text='AIAWVLEN', blank=True, null=True)
	aiagp1 = models.IntegerField(help_text='AIAGP1', blank=True, null=True)
	aiagp2 = models.IntegerField(help_text='AIAGP2', blank=True, null=True)
	aiagp3 = models.IntegerField(help_text='AIAGP3', blank=True, null=True)
	aiagp4 = models.IntegerField(help_text='AIAGP4', blank=True, null=True)
	aiagp5 = models.IntegerField(help_text='AIAGP5', blank=True, null=True)
	aiagp6 = models.IntegerField(help_text='AIAGP6', blank=True, null=True)
	aiagp7 = models.IntegerField(help_text='AIAGP7', blank=True, null=True)
	aiagp8 = models.IntegerField(help_text='AIAGP8', blank=True, null=True)
	aiagp9 = models.IntegerField(help_text='AIAGP9', blank=True, null=True)
	aiagp10 = models.IntegerField(help_text='AIAGP10', blank=True, null=True)
	agt1svy = models.SmallIntegerField(help_text='AGT1SVY', blank=True, null=True)
	agt1svz = models.SmallIntegerField(help_text='AGT1SVZ', blank=True, null=True)
	agt2svy = models.SmallIntegerField(help_text='AGT2SVY', blank=True, null=True)
	agt2svz = models.SmallIntegerField(help_text='AGT2SVZ', blank=True, null=True)
	agt3svy = models.SmallIntegerField(help_text='AGT3SVY', blank=True, null=True)
	agt3svz = models.SmallIntegerField(help_text='AGT3SVZ', blank=True, null=True)
	agt4svy = models.SmallIntegerField(help_text='AGT4SVY', blank=True, null=True)
	agt4svz = models.SmallIntegerField(help_text='AGT4SVZ', blank=True, null=True)
	aimgshen = models.SmallIntegerField(help_text='AIMGSHEN', blank=True, null=True)
	keywddoc = models.TextField(help_text='KEYWDDOC', blank=True)
	series = models.TextField(help_text='SERIES', blank=True)
	recnum = models.BigIntegerField(help_text='RECNUM', blank=False, null=False)
	sunum = models.BigIntegerField(help_text='SUNUM', blank=True, null=True)
	slotnum = models.IntegerField(help_text='SLOTNUM', blank=True, null=True)
	segment = models.TextField(help_text='SEGMENT', blank=True)
