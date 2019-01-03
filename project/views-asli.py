from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from . models import Project, Customer, Order, Partner
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

#view django function
def home_miniportal(request):
	return render(request, 'home_miniportal.html')

def list(request):
	if request.user.is_anonymous():
		# return HttpResponseRedirect(reverse('login'))
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
		return render(request, 'partnerdetail.html', {
														'partner': var_partner,
													})
	else:
		return render(request, 'test.html')
			

def detail(request):
	if request.user.is_anonymous():
		return HttpResponseRedirect(reverse('login')+ '%s'%('?next=') + request.get_full_path())
	# if not request.user.is_staff:
	# 	return HttpResponseRedirect('%s%s%s'%(reverse('login'),'?next=',request.get_full_path()))

	elif request.user.is_staff:
		
		# filter by status
		if request.get_full_path() == '/project/detail':
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
		elif request.get_full_path() == '/project/detail?f=handlebyadj':
			var_projectlist = Project.objects.filter(project_support_lintasarta__exact=20)
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
		elif request.get_full_path() == '/project/detail?f=handlebytla':
			var_projectlist = Project.objects.filter(project_support_lintasarta__exact=30)
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