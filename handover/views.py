from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
# Create your views here.
from . models import Checklistdocument
from . forms import ChecklistdocumentForm

# def index(request):
# 	var_checklistdocument = Checklistdocument.objects.all()
# 	return render(request, 'handover.html', {
# 												'handover': var_checklistdocument,
# 												})
def handoverproject_list(request):
	if request.user.is_anonymous():
		# return HttpResponseRedirect(reverse('login'))
		return HttpResponseRedirect(reverse('login')+ '%s'%('?next=') + request.get_full_path())
	# elif not request.user.is_staff:
	# 	return HttpResponseRedirect('%s%s%s'%(reverse('login'),'?next=',request.get_full_path()))
	elif request.user.is_staff:
		# return HttpResponseRedirect(reverse('penjualan_list'))
		if request.get_full_path() == '/handover/registered':
			var_checklistdocument = Checklistdocument.objects.all()
			return render(request, 'handover_list.html', {
														'handover': var_checklistdocument,
														})
		elif request.get_full_path() == '/handover/registered?f=success':
			var_checklistdocument = Checklistdocument.objects.filter(handover_status=True)
			return render(request, 'handover_list.html', {
														'handover': var_checklistdocument,
														})
		elif request.get_full_path() == '/handover/registered?f=pending':
			var_checklistdocument = Checklistdocument.objects.filter(handover_status=False).order_by('-reminder_date')
			return render(request, 'handover_list.html', {
														'handover': var_checklistdocument,
														})
	else:
		return HttpResponseRedirect(reverse('login'))

def handoverproject(request,random_field):
	var_checklistdocument = Checklistdocument.objects.filter(random_field=random_field)
	return render(request, 'handover.html', {
												'handover': var_checklistdocument,
												})

def handoverproject_screenshot(request,random_field):
	var_checklistdocument = Checklistdocument.objects.filter(random_field=random_field)
	return render(request, 'handover_s.html', {
												'handover': var_checklistdocument,
												})

def handover_dashboard(request):
	var_handover_pending = Checklistdocument.objects.filter(handover_status=False)
	var_handover_success = Checklistdocument.objects.filter(handover_status=True)
	return render(request, 'handover_dashboard.html',{
														'handover_pending': var_handover_pending,
														'handover_success': var_handover_success,
													})

def handover_dashboard_d(request):
	if request.user.is_anonymous():
		return HttpResponseRedirect('%s%s%s'%(reverse('login'),'?next=',request.get_full_path()))
	elif request.user.is_authenticated:
		var_handover_pending = Checklistdocument.objects.filter(handover_status=False)
		var_handover_success = Checklistdocument.objects.filter(handover_status=True)
		total_handover = var_handover_pending.count() + var_handover_success.count()
		percentage_success = round(var_handover_success.count() / total_handover * 100, 2)
		percentage_pending = round(var_handover_pending.count() / total_handover * 100, 2)
		return render(request, 'handover_dashboard_d.html',{
															'handover_pending': var_handover_pending,
															'handover_success': var_handover_success,
															'percentage_success': percentage_success,
															'percentage_pending': percentage_pending,
														})
	else:
		return HttpResponseRedirect(reverse('login'))

## FORM
def input(request):
	if request.method == 'POST':
		form = ChecklistdocumentForm(request.POST, request.FILES)
		if form.is_valid():
			insert = Checklistdocument.objects.create(
															# id=request.POST['id'],
															pic_name=request.POST['pic_name'],
															pic=request.POST['pic'],
					)
		return HttpResponse('image upload success')
	else:
		handover_form = ChecklistdocumentForm()
	return render(request, 'handover_form.html', {'form': handover_form})