from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect
from django.contrib import admin
import biosensorsdb.views

admin.autodiscover()

urlpatterns = patterns('',
  url(r'^admin/', include(admin.site.urls)),
  url(r'^$',      biosensorsdb.views.index, name='index'),
)
