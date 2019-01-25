from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from . models import Project, Projectstatus,Momserahterima, Customer, Order, Partner, Lintasartaperson, Contract, Projectcategory
from datetime import datetime

#custom function
def contract_lessthan3month (rawdata):
	my_list = []
	for data in rawdata:
		contracts = data.contract_set.all()
		for data in contracts:
			calculation = data.end_contract - datetime.now().date()
			if calculation.days < 90:
				lessthan3month = data.project_id
				my_list.append(str(lessthan3month))
	return my_list

def contract_lessthan2month (rawdata):
	my_list = []
	for data in rawdata:
		contracts = data.contract_set.all()
		for data in contracts:
			calculation = data.end_contract - datetime.now().date()
			if calculation.days < 60:
				lessthan2month = data.project_id
				my_list.append(str(lessthan2month))
	return my_list

def list(request):
	if request.user.is_anonymous():
		return HttpResponseRedirect(reverse('login')+ '%s'%('?next=') + request.get_full_path())
	elif request.user.is_authenticated:
		var_projectlist = Project.objects.exclude(project_status__exact=3)
		return render(request, 'projectlist.html', {
														'projectlist': var_projectlist,
													})
	else:
		return HttpResponseRedirect(reverse('login')+ '%s'%('?next=') + request.get_full_path())

def partnerdetail(request, partner_id):
	if request.user.is_anonymous():
		return HttpResponseRedirect(reverse('login')+ '%s'%('?next=') + request.get_full_path())
	elif request.user.is_staff:
		var_partner =  Partner.objects.filter(partner_id__exact=partner_id)
		var_showallproject = Project.objects.all()
		var_parter_by_project = var_showallproject.filter(partner=partner_id)
		#print(var_parter_by_project.count())
		return render(request, 'partnerdetail.html', {
														'partner': var_partner,
														'parter_by_project':var_parter_by_project
													})
	else:
		return render(request, 'test.html')


def kategori(request,kategori):
	if request.user.is_anonymous():
		return HttpResponseRedirect(reverse('login')+ '%s'%('?next=') + request.get_full_path())
	elif request.user.is_staff:
		var_showallproject = Project.objects.all()
		var_kategori = Projectcategory.objects.get(project_category=kategori)
		var_project_project_category = var_showallproject.filter(project_category=var_kategori)
		return render(request, "kategori.html", {
		'project_project_category1':var_project_project_category, 
		'kategorinya' : var_kategori,
		})
	else:
		return render(request, 'test.html')

def customer(request,customer):
	if request.user.is_anonymous():
		return HttpResponseRedirect(reverse('login')+ '%s'%('?next=') + request.get_full_path())
	elif request.user.is_staff:
		var_showallproject = Project.objects.all()
		var_customer = var_showallproject.get(project_id=customer)
		return render(request, "customer.html", {
		'customer' : var_customer,
		'showallproject':var_showallproject,
		})
	else:
		return render(request, 'test.html')

def status(request,status):
	if request.user.is_anonymous():
		return HttpResponseRedirect(reverse('login')+ '%s'%('?next=') + request.get_full_path())
	elif request.user.is_staff:
		var_status = Projectstatus.objects.get(status=status)
		var_showallproject = Project.objects.all()
		var_project_status = var_showallproject.filter(project_status=var_status)
		return render(request, "status.html", {
		'statusnya' : var_status,
		'projectstatusnya' : var_project_status,		
		});
	else:
		return render(request, 'test.html')

def home_miniportal(request):
	if request.user.is_anonymous():
		return HttpResponseRedirect(reverse('login')+ '%s'%('?next=') + request.get_full_path())
	elif request.user.is_authenticated:
		var_showallproject = Project.objects.all()
		var_project_category = Projectcategory.objects.all()
		var_project_project_category1 = var_showallproject.filter(project_category='1')
		var_project_project_category2 = var_showallproject.filter(project_category='2')
		var_project_project_category3 = var_showallproject.filter(project_category='3')
		var_project_project_category4 = var_showallproject.filter(project_category='4')
		var_project_project_category5 = var_showallproject.filter(project_category='5')		
		var_project_project_category6 = var_showallproject.filter(project_category='6')
		#var status project
		var_status_project_ops = var_showallproject.filter(project_status='6')
		var_status_project_isolir = var_showallproject.filter(project_status='5')
		var_status_project_cabut = var_showallproject.filter(project_status='4')
		var_status_project_other = var_showallproject.exclude(project_status='4').exclude(project_status='5').exclude(project_status='6')
		#var filter untuk vendor handle berapa project
		var_project_by_vendor = var_showallproject.exclude(partner='2')
		var_project_by_lmd = var_showallproject.filter(partner='1')
		var_project_by_LA = var_showallproject.filter(partner='2')
		var_project_by_3 = var_showallproject.filter(partner='3')
		var_project_by_4 = var_showallproject.filter(partner='4')
		var_project_by_5 = var_showallproject.filter(partner='5')
		var_project_by_6 = var_showallproject.filter(partner='6')
		var_project_by_7 = var_showallproject.filter(partner='7')
		var_project_by_8 = var_showallproject.filter(partner='8')
		var_project_by_9 = var_showallproject.filter(partner='9')
		var_project_by_10 = var_showallproject.filter(partner='10')
		var_project_by_11 = var_showallproject.filter(partner='11')
		#object contract all
		var_showallcontract = Contract.objects.all()
		var_contract_aro = var_showallcontract.filter(perpanjangan="ARO").count() 
		var_contract_non_aro = var_showallcontract.filter(perpanjangan="NON ARO").count()
		var_contract_aro_notset = var_showallcontract.filter(perpanjangan="").count()
		project_lessthan3month = len(contract_lessthan3month(var_showallproject))
		#object partner all
		var_partner =  Partner.objects.all()
		var_partner_exla =  var_partner.exclude(partner_id='2')
		return render(request, 'index.html', {
														'partnernya': var_partner,
														'partner_exlanya': var_partner_exla,
														'showallprojectnya' : var_showallproject,
														'project_categorynya' : var_project_category,
														'var_project_project_category1nya' : var_project_project_category1,
														'var_project_project_category2nya' : var_project_project_category2,
														'var_project_project_category3nya' : var_project_project_category3,
														'var_project_project_category4nya' : var_project_project_category4,
														'var_project_project_category5nya' : var_project_project_category5,
														'var_project_project_category6nya' : var_project_project_category6,
														'project_by_vendornya' : var_project_by_vendor,
														'project_by_lmdnya' : var_project_by_lmd,
														'project_by_lanya' : var_project_by_LA,
														'project_by_3nya' : var_project_by_3,
														'project_by_4nya' : var_project_by_4,
														'project_by_5nya' : var_project_by_5,
														'project_by_6nya' : var_project_by_6,
														'project_by_7nya' : var_project_by_7,
														'project_by_8nya' : var_project_by_8,
														'project_by_9nya' : var_project_by_9,
														'project_by_10nya' : var_project_by_10,
														'project_by_11nya' : var_project_by_11,
														'showallcontractnya' : var_showallcontract,
														'project_lessthan3monthnya': project_lessthan3month,
														'project_contract_aronya' : var_contract_aro,
														'project_contract_non_aronya' : var_contract_non_aro,
														'project_contract_aro_notsetnya' : var_contract_aro_notset,
														'status_project_ops' : var_status_project_ops,
														'status_project_cabut' : var_status_project_cabut,
														'status_project_isolir' : var_status_project_isolir,
														'status_project_other' : var_status_project_other
													})
	else:
		return HttpResponseRedirect(reverse('login')+ '%s'%('?next=') + request.get_full_path())


def mom(request, mom_id):
	
	if request.user.is_anonymous():
		return HttpResponseRedirect(reverse('login')+ '%s'%('?next=') + request.get_full_path())
	elif request.user.is_staff:
		var_mom = Momserahterima.objects.filter(mom_id__exact=mom_id)
		return render(request, 'mom.html', {
														'momnya': var_mom,
													})
	else:
		return render(request, 'test.html')
		

def showallproject(request):
	if request.user.is_anonymous():
		return HttpResponseRedirect(reverse('login')+ '%s'%('?next=') + request.get_full_path())
	elif request.user.is_authenticated:
		var_showallproject = Project.objects.all()
		var_project_category = Projectcategory.objects.all()
		var_project_project_category1 = var_showallproject.filter(project_category='1')
		var_project_project_category2 = var_showallproject.filter(project_category='2')
		var_project_project_category3 = var_showallproject.filter(project_category='3')
		var_project_project_category4 = var_showallproject.filter(project_category='4')
		var_project_project_category5 = var_showallproject.filter(project_category='5')		
		var_project_project_category6 = var_showallproject.filter(project_category='6')
		#var filter untuk vendor handle berapa project
		var_project_by_vendor = var_showallproject.exclude(partner='2')
		var_project_by_lmd = var_showallproject.filter(partner='1')
		var_project_by_LA = var_showallproject.filter(partner='2')
		var_project_by_3 = var_showallproject.filter(partner='3')
		var_project_by_4 = var_showallproject.filter(partner='4')
		var_project_by_5 = var_showallproject.filter(partner='5')
		var_project_by_6 = var_showallproject.filter(partner='6')
		var_project_by_7 = var_showallproject.filter(partner='7')
		var_project_by_8 = var_showallproject.filter(partner='8')
		var_project_by_9 = var_showallproject.filter(partner='9')
		var_project_by_10 = var_showallproject.filter(partner='10')
		var_project_by_11 = var_showallproject.filter(partner='11')
		#object contract all
		var_showallcontract = Contract.objects.all()
		var_contract_aro = var_showallcontract.filter(perpanjangan="ARO").count() 
		var_contract_non_aro = var_showallcontract.filter(perpanjangan="NON ARO").count()
		var_contract_aro_notset = var_showallcontract.filter(perpanjangan="").count()
		project_lessthan3month = len(contract_lessthan3month(var_showallproject))
		#object partner all
		var_partner =  Partner.objects.all()
		var_partner_exla =  var_partner.exclude(partner_id='2')
		return render(request, 'projectallshow.html', {
														'partnernya': var_partner,
														'partner_exlanya': var_partner_exla,
														'showallprojectnya' : var_showallproject,
														'project_categorynya' : var_project_category,
														'var_project_project_category1nya' : var_project_project_category1,
														'var_project_project_category2nya' : var_project_project_category2,
														'var_project_project_category3nya' : var_project_project_category3,
														'var_project_project_category4nya' : var_project_project_category4,
														'var_project_project_category5nya' : var_project_project_category5,
														'var_project_project_category6nya' : var_project_project_category6,
														'project_by_vendornya' : var_project_by_vendor,
														'project_by_lmdnya' : var_project_by_lmd,
														'project_by_lanya' : var_project_by_LA,
														'project_by_3nya' : var_project_by_3,
														'project_by_4nya' : var_project_by_4,
														'project_by_5nya' : var_project_by_5,
														'project_by_6nya' : var_project_by_6,
														'project_by_7nya' : var_project_by_7,
														'project_by_8nya' : var_project_by_8,
														'project_by_9nya' : var_project_by_9,
														'project_by_10nya' : var_project_by_10,
														'project_by_11nya' : var_project_by_11,
														'showallcontractnya' : var_showallcontract,
														'project_lessthan3monthnya': project_lessthan3month,
														'project_contract_aronya' : var_contract_aro,
														'project_contract_non_aronya' : var_contract_non_aro,
														'project_contract_aro_notsetnya' : var_contract_aro_notset,
													})
	else:
		return HttpResponseRedirect(reverse('login')+ '%s'%('?next=') + request.get_full_path())

def detail(request):
	if request.user.is_anonymous():
		return HttpResponseRedirect(reverse('login')+ '%s'%('?next=') + request.get_full_path())
	# if not request.user.is_staff:
	# 	return HttpResponseRedirect('%s%s%s'%(reverse('login'),'?next=',request.get_full_path()))

	elif request.user.is_staff:
		
		# filter by status
		if request.get_full_path() == '/project/detail':
			var_contract = Contract.objects.all()
			var_contract_partner = var_contract.filter(contract_type='2')
			var_contract_customer = var_contract.filter(contract_type='1')
			var_projectlist = Project.objects.all()
			project_lessthan3month = len(contract_lessthan3month(var_projectlist))
			simple_project_level = var_projectlist.filter(project_level__exact='s').count()
			medium_project_level = var_projectlist.filter(project_level__exact='m').count()
			complex_project_level = var_projectlist.filter(project_level__exact='c').count()
			return render(request, 'projectdetail.html', {
															'projectlist': var_projectlist,
															'project_lessthan3month': project_lessthan3month,
															'simple_project_level': simple_project_level,
															'medium_project_level': medium_project_level,
															'complex_project_level': complex_project_level,
															'contract_partnernya' : var_contract_partner,
															'contract_customernya' : var_contract_customer,
														})

		elif request.get_full_path() == '/project/detail?f=ops':
			var_projectlist = Project.objects.exclude(project_status__exact=3)
			project_lessthan3month = len(contract_lessthan3month(var_projectlist))
			simple_project_level = var_projectlist.filter(project_level__exact='s').count()
			medium_project_level = var_projectlist.filter(project_level__exact='m').count()
			complex_project_level = var_projectlist.filter(project_level__exact='c').count()
			return render(request, 'projectdetail.html', {
															'projectlist': var_projectlist,
															'project_lessthan3month': project_lessthan3month,
															'simple_project_level': simple_project_level,
															'medium_project_level': medium_project_level,
															'complex_project_level': complex_project_level,
														})
		elif request.get_full_path() == '/project/detail?f=tidak-lengkap':
			var_projectlist = Project.objects.filter(project_status__exact=1)
			project_lessthan3month = len(contract_lessthan3month(var_projectlist))
			simple_project_level = var_projectlist.filter(project_level__exact='s').count()
			medium_project_level = var_projectlist.filter(project_level__exact='m').count()
			complex_project_level = var_projectlist.filter(project_level__exact='c').count()
			return render(request, 'projectdetail.html', {
															'projectlist': var_projectlist,
															'project_lessthan3month': project_lessthan3month,
															'simple_project_level': simple_project_level,
															'medium_project_level': medium_project_level,
															'complex_project_level': complex_project_level,
														})
		elif request.get_full_path() == '/project/detail?f=lengkap':
			var_projectlist = Project.objects.filter(project_status__exact=2)
			project_lessthan3month = len(contract_lessthan3month(var_projectlist))
			simple_project_level = var_projectlist.filter(project_level__exact='s').count()
			medium_project_level = var_projectlist.filter(project_level__exact='m').count()
			complex_project_level = var_projectlist.filter(project_level__exact='c').count()
			return render(request, 'projectdetail.html', {
															'projectlist': var_projectlist,
															'project_lessthan3month': project_lessthan3month,
															'simple_project_level': simple_project_level,
															'medium_project_level': medium_project_level,
															'complex_project_level': complex_project_level,
														})
		elif request.get_full_path() == '/project/detail?f=delivery':
			var_projectlist = Project.objects.filter(project_status__exact=3)
			project_lessthan3month = len(contract_lessthan3month(var_projectlist))
			simple_project_level = var_projectlist.filter(project_level__exact='s').count()
			medium_project_level = var_projectlist.filter(project_level__exact='m').count()
			complex_project_level = var_projectlist.filter(project_level__exact='c').count()
			return render(request, 'projectdetail.html', {
															'projectlist': var_projectlist,
															'project_lessthan3month': project_lessthan3month,
															'simple_project_level': simple_project_level,
															'medium_project_level': medium_project_level,
															'complex_project_level': complex_project_level,
														})
		
		# filter by handle by
		elif request.get_full_path() == '/project/detail?f=handlebyhbi':
			var_projectlist = Project.objects.filter(project_support_lintasarta__exact=1)
			project_lessthan3month = len(contract_lessthan3month(var_projectlist))
			simple_project_level = var_projectlist.filter(project_level__exact='s').count()
			medium_project_level = var_projectlist.filter(project_level__exact='m').count()
			complex_project_level = var_projectlist.filter(project_level__exact='c').count()
			return render(request, 'projectdetail.html', {
															'projectlist': var_projectlist,
															'project_lessthan3month': project_lessthan3month,
															'simple_project_level': simple_project_level,
															'medium_project_level': medium_project_level,
															'complex_project_level': complex_project_level,
														})
		elif request.get_full_path() == '/project/detail?f=handlebyrdq':
			var_projectlist = Project.objects.filter(project_support_lintasarta__exact=96)
			project_lessthan3month = len(contract_lessthan3month(var_projectlist))
			simple_project_level = var_projectlist.filter(project_level__exact='s').count()
			medium_project_level = var_projectlist.filter(project_level__exact='m').count()
			complex_project_level = var_projectlist.filter(project_level__exact='c').count()
			return render(request, 'projectdetail.html', {
															'projectlist': var_projectlist,
															'project_lessthan3month': project_lessthan3month,
															'simple_project_level': simple_project_level,
															'medium_project_level': medium_project_level,
															'complex_project_level': complex_project_level,
														})
		elif request.get_full_path() == '/project/detail?f=handlebyrjr':
			var_projectlist = Project.objects.filter(project_support_lintasarta__exact=95)
			project_lessthan3month = len(contract_lessthan3month(var_projectlist))
			simple_project_level = var_projectlist.filter(project_level__exact='s').count()
			medium_project_level = var_projectlist.filter(project_level__exact='m').count()
			complex_project_level = var_projectlist.filter(project_level__exact='c').count()
			return render(request, 'projectdetail.html', {
															'projectlist': var_projectlist,
															'project_lessthan3month': project_lessthan3month,
															'simple_project_level': simple_project_level,
															'medium_project_level': medium_project_level,
															'complex_project_level': complex_project_level,
														})


		# filter by contract status
		elif request.get_full_path() == '/project/detail?f=contractlessthan3month':
			var_projectlist = Project.objects.all()
			project_id = contract_lessthan3month(var_projectlist)
			var_projectlist = Project.objects.filter(pk__in=project_id)
			project_lessthan3month = var_projectlist.count()
			simple_project_level = var_projectlist.filter(project_level__exact='s').count()
			medium_project_level = var_projectlist.filter(project_level__exact='m').count()
			complex_project_level = var_projectlist.filter(project_level__exact='c').count()
			return render(request, 'projectdetail.html', {
															'projectlist': var_projectlist,
															'project_lessthan3month': project_lessthan3month,
															'simple_project_level': simple_project_level,
															'medium_project_level': medium_project_level,
															'complex_project_level': complex_project_level,
														})

		# others
		# else:

	else:
		return HttpResponseRedirect(reverse('login'))

		##contract_set