from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^', include('traits_web_prototype.urls', namespace='traits_web_prototype')),
    url(r'^admin/', include(admin.site.urls)),
)


