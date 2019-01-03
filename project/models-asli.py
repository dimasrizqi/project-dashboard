from django.db import models

# Create your models here.
class Projectstatus(models.Model):
	project_status_id = models.AutoField(primary_key=True)
	status = models.CharField(max_length=100)

	def __str__(self):
		return self.status

class Customer(models.Model):
	customer_id = models.AutoField(primary_key=True)
	customer_name = models.CharField(max_length=100)
	customersegment = models.ForeignKey('Customersegment')
	customer_ho_address = models.CharField(max_length=100,blank=True)
	customer_contact = models.CharField(max_length=100,blank=True)

	def __str__(self):
		return self.customer_name

class Customersegment(models.Model):
	customer_segment_id = models.AutoField(primary_key=True)
	customer_segment = models.CharField(max_length=100)

	def __str__(self):
		return self.customer_segment

class Project(models.Model):
	chose_project_level = (
		('c', 'Complex'),
		('m', 'Medium'),
		('s', 'Simple'),
	)

	chose_sla_support_hour = (
		('24x7', '24x7'),
		('8x5', '8x5'),
	)

	project_id = models.AutoField(primary_key=True)
	customer = models.ManyToManyField('Customer')
	partner = models.ManyToManyField('Partner')
	project_name = models.CharField(max_length=100)
	project_status = models.ForeignKey('Projectstatus')
	project_level = models.CharField(max_length=1, choices=chose_project_level)
	
	##Scope
	# summary_scope = models.ForeignKey('Scope')
	scope_detail = models.TextField(max_length=1000)
	scope_summary = models.TextField(max_length=500)

	##SLA
	# sla = models.ForeignKey('Servicelevelagreement')
	sla_availability = models.CharField(max_length=5)
	sla_support_hour = models.CharField(max_length=5, choices=chose_sla_support_hour)
	sla_response_time = models.CharField(max_length=50)
	sla_resolution_time = models.CharField(max_length=50)


	descriptions = models.CharField(max_length=100,blank=True)
	project_date_handover = models.DateField(auto_now=False, auto_now_add=False)
	topology = models.ImageField(upload_to = 'project/static/img/topo/', default = 'project/static/img/topo/no-img.jpg')
	
	##Contract
	contract_customer = models.CharField(max_length=500)
	contract_partner = models.CharField(max_length=500)

	## PO & Approval
	purchase_order = models.CharField(max_length=500)
	project_approval = models.CharField(max_length=500)
	
	## proposal to customer detail
	proposal_to_customer = models.CharField(max_length=500)
	proposal_to_customer_sow = models.CharField(max_length=500)
	proposal_to_customer_hld = models.CharField(max_length=500)
	proposal_to_customer_boq = models.CharField(max_length=500)
	
	## proposal to partner detail
	proposal_from_partner = models.CharField(max_length=500)
	proposal_from_partner_sow = models.CharField(max_length=500)
	proposal_from_partner_boq = models.CharField(max_length=500)

	## implementation
	## implementation document
	implementation_document = models.CharField(max_length=500)
	technical_data = models.CharField(max_length=500)

	low_level_design = models.CharField(max_length=500)
	business_case  = models.CharField(max_length=500)
	user_acceptance_test = models.CharField(max_length=500)
	bast_to_customer = models.CharField(max_length=500)

	## related to partner
	partner_document  = models.TextField(max_length=1000)
	product_spesification  = models.CharField(max_length=500)
	bast_from_partner = models.CharField(max_length=500)

	## working instruction
	wi_operation  = models.CharField(max_length=500)
	wi_customer_care = models.CharField(max_length=500)
	
	## contact person
	project_support_lintasarta = models.ForeignKey('Lintasartaperson',related_name='project_support_lintasarta')
	car_lintasarta = models.ForeignKey('Lintasartaperson',related_name='car_lintasarta')
	sales_lintasarta = models.ForeignKey('Lintasartaperson',related_name='sales_lintasarta')
	delivery_lintasarta = models.ForeignKey('Lintasartaperson',related_name='delivery_lintasarta')
	sa_lintasarta = models.ForeignKey('Lintasartaperson',related_name='sa_lintasarta')

	table_updated = models.DateField(auto_now=True, auto_now_add=False)
	table_creation_timestamp = models.DateField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return "%s & Project %s " % (self.customer.all()[0], self.project_name)

class Partner(models.Model):
	partner_id = models.AutoField(primary_key=True)
	partner_name = models.CharField(max_length=100)
	partner_address = models.CharField(max_length=100,blank=True)
	partner_web = models.CharField(max_length=100,blank=True)
	contact_sales_name = models.CharField(max_length=100,blank=True)
	contact_sales_email = models.CharField(max_length=100,blank=True)
	contact_sales_telp = models.CharField(max_length=100,blank=True)
	contact_support_name = models.CharField(max_length=100,blank=True)
	contact_support_email = models.CharField(max_length=100,blank=True)
	contact_support_telp = models.CharField(max_length=100,blank=True)
	contact_support_web = models.CharField(max_length=100,blank=True)
	contact_manager_name = models.CharField(max_length=100,blank=True)
	contact_manager_email = models.CharField(max_length=100,blank=True)
	contact_manager_telp = models.CharField(max_length=100,blank=True)
	contact_manager_telp = models.CharField(max_length=100,blank=True)
	
	def __str__(self):
		return self.partner_name

class Order(models.Model):
	order_id = models.AutoField(primary_key=True)
	project = models.ForeignKey('Project')
	no_jaringan = models.CharField(max_length=10)
	keterangan = models.TextField(max_length=500)
	jasa = models.CharField(max_length=100)
	jenis_kecepatan = models.CharField(max_length=100,blank=True)
	kecepatan = models.CharField(max_length=100,blank=True)

	def __str__(self):
		return "%s - %s" % (self.no_jaringan, self.project)

class Contract(models.Model):
	contract_id = models.AutoField(primary_key=True)
	project = models.ForeignKey('Project')
	contract_type = models.ForeignKey('Contracttype')
	no_contract = models.CharField(max_length=100,blank=True)
	start_contract = models.DateField(auto_now=False, auto_now_add=False)
	end_contract = models.DateField(auto_now=False, auto_now_add=False)

	def __str__(self):

		return "%s - %s - %s" % (self.no_contract, self.contract_type, self.project)

class Contracttype(models.Model):
	contract_type_id = models.AutoField(primary_key=True)
	contract_type = models.CharField(max_length=100)

	def __str__(self):
		return self.contract_type

class Lintasartaperson(models.Model):
	initial = models.CharField(max_length=3)
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100,blank=True)
	telp = models.CharField(max_length=100,blank=True)

	def __str__(self):
		return "%s - %s" % (self.initial, self.name)