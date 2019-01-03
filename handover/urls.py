from django.conf.urls import url

from . import views

app_name = 'handover'
urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^input$', views.input, name='input'),
    url(r'^registered$', views.handoverproject_list, name='handover_list'),
    url(r'^dashboard/$', views.handover_dashboard, name='handover_dashboard'),
    url(r'^dashboard/detail$', views.handover_dashboard_d, name='handover_dashboard_d'),
    url(r'^(?P<random_field>[0-9]{7})/$', views.handoverproject, name='handoverproject'),
    url(r'^(?P<random_field>[0-9]{7})/s$', views.handoverproject_screenshot, name='handoverproject_s'),
]