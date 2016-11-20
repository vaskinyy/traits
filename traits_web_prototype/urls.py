from django.conf.urls import patterns, url
from traits_web_prototype import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^paternity/$', views.paternity, name='paternity'),
    url(r'^parental/$', views.parental, name='parental'),
    url(r'^offspring/$', views.offspring, name='offspring'),
    url(r'^grandparent/$', views.grandparent, name='grandparent'),
)

