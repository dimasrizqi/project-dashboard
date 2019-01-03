from django import forms
from . models import Checklistdocument

class ChecklistdocumentForm(forms.ModelForm):
	
	class Meta:
		model = Checklistdocument
		fields = [
				'customer_name',
				'project_name',
				'scope_of_work',
				'project_approval',
				'purchase_order',
				'sla',
				'business_case',
				'proposal_to_customer_hld',
				'partner_document_so_spk',
				'proposal_to_customer_tda',
				'implementation_document_lld',
				'wi_operation',
				'wi_customer_care',
				'contact_person_customer_vendor',
				'handover_budget',
				'user_acceptance_test',
				'bast_to_customer',
				'bast_from_partner',
				'no_jaringan_acuan',
				'notes',
		]