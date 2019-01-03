from django.conf.urls import url

from . import views

app_name = 'asset'
urlpatterns = [
    url(r'^list$', views.assetlist, name='assetlist'),
]