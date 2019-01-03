from django.conf.urls import url

from . import views

app_name = 'project'
urlpatterns = [
    url(r'^detail$', views.detail, name='detail'),
    url(r'^list$', views.list, name='list'),
    # url(r'^partner$', views.partnerdetail, name='partner'),
    # url(r'^partner(?P<pk>[0-9]{7})/$', views.handoverproject, name='handoverproject'),
    url(r'^partner/(?P<partner_id>[0-9]+)$', views.partnerdetail, name='partner'),


]