from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$','animal.views.index'),
	url(r'^validar/$', 'animal.views.validar'),
)