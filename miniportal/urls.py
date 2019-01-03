"""miniportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from project import views as miniportal_views
from handover import views as handover_views

admin.site.site_header = "Miniportal Admin"
admin.site.site_title = "Miniportal site admin"
# admin.site.index_title = "Site administration "

urlpatterns = [
    url(r'^$', miniportal_views.home_miniportal , name='home'),
    url(r'^project/', include('project.urls')),
    url(r'^handover/', include('handover.urls')),
    url(r'^asset/', include('asset.urls')),
    url(r'^admin/', admin.site.urls),

    # url(r'^accounts/login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),

    url(r'^jet/', include('jet.urls', 'jet')), # Django JET URLS
]
