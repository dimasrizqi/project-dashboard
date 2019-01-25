from django.conf.urls import url
from project import views as miniportal_views

from . import views

app_name = 'project'
urlpatterns = [
	url(r'^$', miniportal_views.home_miniportal ),
    url(r'^partner/$', miniportal_views.home_miniportal ),
    url(r'^kategori/$', miniportal_views.home_miniportal ),
    url(r'^status/$', miniportal_views.home_miniportal ),
    url(r'^(?P<customer>[0-9]+)$', views.customer),
    url(r'^detail$', views.detail, name='detail'),
    url(r'^list$', views.list, name='list'),
    url(r'^showallproject$', views.showallproject, name='All Project list'),
    url(r'^partner/(?P<partner_id>[0-9\w]+)$', views.partnerdetail, name='partner'),
    url(r'^kategori/(?P<kategori>[\w\s]+)/$', views.kategori),
    url(r'^mom/(?P<mom_id>[0-9]+)$', views.mom, name='mom'),
    url(r'^status/(?P<status>[\w\s]+)/$', views.status),
   
]
