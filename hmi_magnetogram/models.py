from __future__ import unicode_literals

from django.db import models
from common.models import BaseMetaData, BaseKeyword, BaseDataLocation, BaseTag

class MetaData(BaseMetaData):
	date = models.DateTimeField(help_text='DATE', blank=True, null=True)
	date_obs = models.DateTimeField(help_text='DATE-OBS', blank=True, null=True)
	telescop = models.TextField(help_text='TELESCOP', blank=True)
	instrume = models.TextField(help_text='INSTRUME', blank=True)
	wavelnth = models.FloatField(help_text='WAVELNTH', blank=True, null=True)
	camera = models.IntegerField(help_text='CAMERA', blank=True, null=True)
	bunit = models.TextField(help_text='BUNIT', blank=True)
	origin = models.TextField(help_text='ORIGIN', blank=True)
	content = models.TextField(help_text='CONTENT', blank=True)
	quality = models.IntegerField(help_text='QUALITY', blank=True, null=True)
	quallev1 = models.IntegerField(help_text='QUALLEV1', blank=True, null=True)
	bld_vers = models.TextField(help_text='BLD_VERS', blank=True)
	hcamid = models.IntegerField(help_text='HCAMID', blank=True, null=True)
	source = models.TextField(help_text='SOURCE', blank=True)
	totvals = models.IntegerField(help_text='TOTVALS', blank=True, null=True)
	datavals = models.IntegerField(help_text='DATAVALS', blank=True, null=True)
	missvals = models.IntegerField(help_text='MISSVALS', blank=True, null=True)
	satvals = models.IntegerField(help_text='SATVALS', blank=True, null=True)
	datamin2 = models.FloatField(help_text='DATAMIN2', blank=True, null=True)
	datamax2 = models.FloatField(help_text='DATAMAX2', blank=True, null=True)
	datamed2 = models.FloatField(help_text='DATAMED2', blank=True, null=True)
	datamea2 = models.FloatField(help_text='DATAMEA2', blank=True, null=True)
	datarms2 = models.FloatField(help_text='DATARMS2', blank=True, null=True)
	dataske2 = models.FloatField(help_text='DATASKE2', blank=True, null=True)
	datakur2 = models.FloatField(help_text='DATAKUR2', blank=True, null=True)
	datamin = models.FloatField(help_text='DATAMIN', blank=True, null=True)
	datamax = models.FloatField(help_text='DATAMAX', blank=True, null=True)
	datamedn = models.FloatField(help_text='DATAMEDN', blank=True, null=True)
	datamean = models.FloatField(help_text='DATAMEAN', blank=True, null=True)
	datarms = models.FloatField(help_text='DATARMS', blank=True, null=True)
	dataskew = models.FloatField(help_text='DATASKEW', blank=True, null=True)
	datakurt = models.FloatField(help_text='DATAKURT', blank=True, null=True)
	ctype1 = models.TextField(help_text='CTYPE1', blank=True)
	ctype2 = models.TextField(help_text='CTYPE2', blank=True)
	crpix1 = models.FloatField(help_text='CRPIX1', blank=True, null=True)
	crpix2 = models.FloatField(help_text='CRPIX2', blank=True, null=True)
	crval1 = models.FloatField(help_text='CRVAL1', blank=True, null=True)
	crval2 = models.FloatField(help_text='CRVAL2', blank=True, null=True)
	cdelt1 = models.FloatField(help_text='CDELT1', blank=True, null=True)
	cdelt2 = models.FloatField(help_text='CDELT2', blank=True, null=True)
	cunit1 = models.TextField(help_text='CUNIT1', blank=True)
	cunit2 = models.TextField(help_text='CUNIT2', blank=True)
	crota2 = models.FloatField(help_text='CROTA2', blank=True, null=True)
	crder1 = models.FloatField(help_text='CRDER1', blank=True, null=True)
	crder2 = models.FloatField(help_text='CRDER2', blank=True, null=True)
	csyser1 = models.FloatField(help_text='CSYSER1', blank=True, null=True)
	csyser2 = models.FloatField(help_text='CSYSER2', blank=True, null=True)
	wcsname = models.TextField(help_text='WCSNAME', blank=True)
	dsun_obs = models.FloatField(help_text='DSUN_OBS', blank=True, null=True)
	dsun_ref = models.FloatField(help_text='DSUN_REF', blank=True, null=True)
	rsun_ref = models.FloatField(help_text='RSUN_REF', blank=True, null=True)
	crln_obs = models.FloatField(help_text='CRLN_OBS', blank=True, null=True)
	crlt_obs = models.FloatField(help_text='CRLT_OBS', blank=True, null=True)
	car_rot = models.IntegerField(help_text='CAR_ROT', blank=True, null=True)
	obs_vr = models.FloatField(help_text='OBS_VR', blank=True, null=True)
	obs_vw = models.FloatField(help_text='OBS_VW', blank=True, null=True)
	obs_vn = models.FloatField(help_text='OBS_VN', blank=True, null=True)
	rsun_obs = models.FloatField(help_text='RSUN_OBS', blank=True, null=True)
	t_obs = models.DateTimeField(help_text='T_OBS', blank=True, null=True)
	t_rec = models.DateTimeField(help_text='T_REC', blank=True, null=True)
	cadence = models.FloatField(help_text='CADENCE', blank=True, null=True)
	datasign = models.IntegerField(help_text='DATASIGN', blank=True, null=True)
	hflid = models.IntegerField(help_text='HFLID', blank=True, null=True)
	hcftid = models.IntegerField(help_text='HCFTID', blank=True, null=True)
	qlook = models.IntegerField(help_text='QLOOK', blank=True, null=True)
	cal_fsn = models.IntegerField(help_text='CAL_FSN', blank=True, null=True)
	lutquery = models.TextField(help_text='LUTQUERY', blank=True)
	tsel = models.FloatField(help_text='TSEL', blank=True, null=True)
	tfront = models.FloatField(help_text='TFRONT', blank=True, null=True)
	tintnum = models.IntegerField(help_text='TINTNUM', blank=True, null=True)
	sintnum = models.IntegerField(help_text='SINTNUM', blank=True, null=True)
	distcoef = models.TextField(help_text='DISTCOEF', blank=True)
	rotcoef = models.TextField(help_text='ROTCOEF', blank=True)
	odicoeff = models.IntegerField(help_text='ODICOEFF', blank=True, null=True)
	orocoeff = models.IntegerField(help_text='OROCOEFF', blank=True, null=True)
	polcalm = models.IntegerField(help_text='POLCALM', blank=True, null=True)
	codever0 = models.TextField(help_text='CODEVER0', blank=True)
	codever1 = models.TextField(help_text='CODEVER1', blank=True)
	codever2 = models.TextField(help_text='CODEVER2', blank=True)
	codever3 = models.TextField(help_text='CODEVER3', blank=True)
	calver64 = models.BigIntegerField(help_text='CALVER64', blank=True, null=True)
	series = models.TextField(help_text='SERIES', blank=True)
	recnum = models.BigIntegerField(help_text='RECNUM', blank=False, null=False)
	sunum = models.BigIntegerField(help_text='SUNUM', blank=True, null=True)
	slotnum = models.IntegerField(help_text='SLOTNUM', blank=True, null=True)
	segment = models.TextField(help_text='SEGMENT', blank=True)
	
	class Meta(BaseMetaData.Meta):
		pass

class DataLocation(BaseDataLocation):
	meta_data = models.OneToOneField(MetaData, primary_key=True, db_column = "id", on_delete=models.CASCADE, related_name="data_location")
	
	class Meta(BaseDataLocation.Meta):
		pass


class Keyword(BaseKeyword):
	
	class Meta(BaseKeyword.Meta):
		pass


class Tag(BaseTag):	
	
	class Meta(BaseTag.Meta):
		pass
