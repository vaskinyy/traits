from django.conf.urls import patterns, url
from traits_web_prototype import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)

