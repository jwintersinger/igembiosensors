from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'igembiosensors.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', lambda request: HttpResponseRedirect('/admin/')),
    url(r'^admin/', include(admin.site.urls)),
)
