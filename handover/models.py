from django.db import models
from random import  randint
# from random import choice, randint
# from string import ascii_uppercase, digits
from datetime import datetime

# Create your models here.
class Checklistdocument(models.Model):
	# gen4 = ''.join(choice(ascii_uppercase+digits) for _ in range(4))
	gen4 = str(randint(0,9999))
	ref_id = gen4 + str(datetime.now().time().microsecond)[-3:]

	checklistdocument_id = models.AutoField(primary_key=True)
	# random_field = models.IntegerField(primary_key=True,max_length=7, unique=True, default=ref_id)
	random_field = models.CharField(max_length=7, unique=True, default=ref_id, blank=True)

	# pm/dco
	projectmanager = models.ForeignKey('project.Lintasartaperson')

	# date
	handover_date = models.DateField(auto_now=False, auto_now_add=False)
	reminder_date = models.DateField(auto_now=False, auto_now_add=False)

	## project name & customer name
	customer_name = models.CharField(max_length=100)
	project_name = models.CharField(max_length=200)

	##handover status
	handover_status = models.BooleanField()
	handover_status_remark = models.TextField(blank=True)

	##form checklist
	form_handover = models.BooleanField()
	form_bast = models.BooleanField()
	
	##Checklist
	scope_of_work = models.BooleanField()
	scope_of_work_remark = models.CharField(max_length=200, blank=True)
	
	project_approval = models.BooleanField()
	project_approval_remark = models.CharField(max_length=200, blank=True)

	purchase_order = models.BooleanField()
	purchase_order_remark = models.CharField(max_length=200, blank=True)

	sla = models.BooleanField()
	sla_remark = models.CharField(max_length=200, blank=True)

	business_case = models.BooleanField()
	business_case_remark = models.CharField(max_length=200, blank=True)

	proposal_to_customer_hld = models.BooleanField()
	proposal_to_customer_hld_remark = models.CharField(max_length=200, blank=True)

	proposal_to_customer_tda = models.BooleanField()
	proposal_to_customer_tda_remark = models.CharField(max_length=200, blank=True)

	partner_document_so_spk = models.BooleanField()
	partner_document_so_spk_remark = models.CharField(max_length=200, blank=True)

	product_spesification = models.BooleanField()
	product_spesification_remark = models.CharField(max_length=200, blank=True)

	implementation_document_lld = models.BooleanField()
	implementation_document_lld_remark = models.CharField(max_length=200, blank=True)

	wi_operation  = models.BooleanField()
	wi_operation_remark = models.CharField(max_length=200, blank=True)

	wi_customer_care = models.BooleanField()
	wi_customer_care_remark = models.CharField(max_length=200, blank=True)

	contact_person_customer_vendor = models.BooleanField()
	contact_person_customer_vendor_remark = models.CharField(max_length=200, blank=True)

	handover_budget = models.BooleanField()
	handover_budget_remark = models.CharField(max_length=200, blank=True)

	user_acceptance_test = models.BooleanField()
	user_acceptance_test_remark = models.CharField(max_length=200, blank=True)

	bast_to_customer = models.BooleanField()
	bast_to_customer_remark = models.CharField(max_length=200, blank=True)

	bast_from_partner = models.BooleanField()
	bast_from_partner_remark = models.CharField(max_length=200, blank=True)

	no_jaringan_acuan = models.BooleanField()
	no_jaringan_acuan_remark = models.CharField(max_length=200, blank=True)

	notes = models.CharField(max_length=200)

	table_updated = models.DateField(auto_now=True, auto_now_add=False)
	table_creation_timestamp = models.DateField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return "%s & Project %s " % (self.customer_name, self.project_name)