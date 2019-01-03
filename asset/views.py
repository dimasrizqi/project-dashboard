from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Assetmaster

# Create your views here.
def assetlist(request):
	if request.user.is_anonymous():
		return HttpResponseRedirect('%s%s%s'%(reverse('login'),'?next=',request.get_full_path()))
	elif request.user.is_authenticated:
		asset = Assetmaster.objects.all()
		return render(request, 'assetlist.html', {
													'asset': asset,
													})
	else:
		return HttpResponseRedirect(reverse('login'))