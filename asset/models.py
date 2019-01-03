from django.db import models
# from project.models import Project

# Create your models here.
class Assetmaster(models.Model):
	asset_master_id = models.AutoField(primary_key=True)
	project = models.ForeignKey('project.Project')
	asset = models.ForeignKey('Device')
	sn = models.CharField(max_length=100)
	no_registrasi = models.CharField(max_length=100)
	location = models.TextField(max_length=500,blank=True)
	remark = models.TextField(max_length=500,blank=True)
	# qty = models.IntegerField(max_length=100)

	table_updated = models.DateField(auto_now=True, auto_now_add=False)
	table_creation_timestamp = models.DateField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return "%s - %s - %s - %s" % (self.asset, self.sn, self.no_registrasi, self.project.customer.all()[0])

class Device(models.Model):
	chose_type_device = (
		('hw', 'Hardware'),
		('sw', 'Software'),
	)

	device_id = models.AutoField(primary_key=True)
	device_name = models.CharField(max_length=100)
	device_type = models.CharField(max_length=2, choices=chose_type_device)
	spec = models.TextField(max_length=500)
	
	def __str__(self):
		return self.device_name

class License(models.Model):
	chose_type_license = (
		('sub', 'Subsciption'),
		('sup', 'Support'),
		('per', 'Perpetual'),
	)

	license_id = models.AutoField(primary_key=True)
	asset_master = models.ForeignKey('Assetmaster')
	license_name = models.CharField(max_length=100)
	type_license = models.CharField(max_length=3, choices=chose_type_license)
	license_start_date = models.DateField(auto_now=False, auto_now_add=False)
	license_end_date = models.DateField(auto_now=False, auto_now_add=False)
	remark = models.TextField(max_length=500,blank=True)

	def __str__(self):
		return "%s - %s" % (self.license_name, self.asset_master.asset.device_name)
