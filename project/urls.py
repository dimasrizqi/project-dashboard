from django.conf.urls import url

from . import views

app_name = 'project'
urlpatterns = [
	
    url(r'^detail$', views.detail, name='detail'),
    url(r'^list$', views.list, name='list'),
    url(r'^showallproject$', views.showallproject, name='All Project list'),
    url(r'^partner/(?P<partner_id>[0-9]+)$', views.partnerdetail, name='partner'),
    url(r'^(?P<customer>[0-9]+)$', views.customer),
    url(r'^kategori/(?P<kategori>[\w\s]+)/$', views.kategori),
    url(r'^status/(?P<status>[\w\s]+)/$', views.status),
    url(r'^partner/LMD/$', views.partnerlmd ),
    url(r'^partner/LA/$', views.partnerla),
    url(r'^partner/IBID/$', views.partneribid),
    url(r'^partner/IBM/$', views.partneribm),
    url(r'^partner/BIT/$', views.partnerbit),
    url(r'^partner/IKI/$', views.partneriki),
    url(r'^partner/DNN/$', views.partnerdnn),
    url(r'^partner/MSI/$', views.partnermsi),
    url(r'^partner/INDST/$', views.partnerindst),
    url(r'^partner/AST/$', views.partnerast),
    url(r'^partner/BPT/$', views.partnerbpt),
    url(r'^mom/(?P<mom_id>[0-9]+)$', views.mom, name='mom'),
   
]
