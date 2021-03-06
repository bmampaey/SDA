from __future__ import unicode_literals
from django.db import models
from .base import BaseMetadata

class Eit(BaseMetadata):
	blocks_horz = models.IntegerField('BLOCKS_HORZ', help_text='None', blank=True, null=True)
	blocks_vert = models.IntegerField('BLOCKS_VERT', help_text='None', blank=True, null=True)
	camera_err = models.TextField('CAMERA_ERR', help_text='None', blank=True, null=True)
	car_rot = models.FloatField('CAR_ROT', help_text='Carrington rotation at earth ', blank=True, null=True)
	ccdtemp = models.FloatField('CCDTEMP', help_text='CCD temperature (DN/100) ', blank=True, null=True)
	cdelt1 = models.FloatField('CDELT1', help_text='Pixel scale x', blank=True, null=True)
	cdelt2 = models.FloatField('CDELT2', help_text='Pixel scale y', blank=True, null=True)
	cftemp = models.FloatField('CFTEMP', help_text='CCD cold finger temperature', blank=True, null=True)
	cmp_no = models.IntegerField('CMP_NO', help_text='Unique campaign instance (1 = synoptic) ', blank=True, null=True)
	commanded_exposure_time = models.TextField('COMMANDED_EXPOSURE_TIME', help_text='', blank=True, null=True)
	corrected_date_obs = models.DateTimeField('CORRECTED_DATE_OBS', help_text='', blank=True, null=True)
	crpix1 = models.FloatField('CRPIX1', help_text='Sun center x, EIT pixels', blank=True, null=True)
	crpix2 = models.FloatField('CRPIX2', help_text='Sun center y, EIT pixels', blank=True, null=True)
	datasrc = models.TextField('DATASRC', help_text='None', blank=True, null=True)
	date = models.DateTimeField('DATE', help_text='Date of file creation', blank=True, null=True)
	date_obs = models.DateTimeField('DATE_OBS', help_text='UTC at spacecraft ', blank=True, null=True)
	expmode = models.TextField('EXPMODE', help_text='None', blank=True, null=True)
	exptime = models.FloatField('EXPTIME', help_text='Exposure time (total commanded + shutter close)', blank=True, null=True)
	filename = models.TextField('FILENAME', help_text='None', blank=True, null=True)
	filter = models.TextField('FILTER', help_text='None', blank=True, null=True)
	image_of_seq = models.IntegerField('IMAGE_OF_SEQ', help_text='None', blank=True, null=True)
	instrume = models.TextField('INSTRUME', help_text='None', blank=True, null=True)
	leb_proc = models.TextField('LEB_PROC', help_text='None', blank=True, null=True)
	line_sync = models.TextField('LINE_SYNC', help_text='None', blank=True, null=True)
	n_missing_blocks = models.IntegerField('N_MISSING_BLOCKS', help_text='None', blank=True, null=True)
	num_leb_proc = models.IntegerField('NUM_LEB_PROC', help_text='None', blank=True, null=True)
	object = models.TextField('OBJECT', help_text='None', blank=True, null=True)
	obs_prog = models.TextField('OBS_PROG', help_text='None', blank=True, null=True)
	origin = models.TextField('ORIGIN', help_text='Rocket Science = NASA GSFC', blank=True, null=True)
	readout_port = models.TextField('READOUT_PORT', help_text='None', blank=True, null=True)
	sci_obj = models.TextField('SCI_OBJ', help_text='None', blank=True, null=True)
	sc_roll = models.FloatField('SC_ROLL', help_text='s/c roll (Solar north + CCW from nominal)', blank=True, null=True)
	shutter_close_time = models.TextField('SHUTTER_CLOSE_TIME', help_text='', blank=True, null=True)
	solar_b0 = models.FloatField('SOLAR_B0', help_text='', blank=True, null=True)
	solar_r = models.FloatField('SOLAR_R', help_text='Solar photospheric radius, EIT pixels', blank=True, null=True)
	telescop = models.TextField('TELESCOP', help_text='None', blank=True, null=True)
	wavelnth = models.IntegerField('WAVELNTH', help_text='Wavelength 284 / 171 = Fe IX/X, 195 = Fe XII, / 284 = Fe XV, 304 = He ', blank=True, null=True)
