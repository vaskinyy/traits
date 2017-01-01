from django.conf.urls import patterns, url
from traits_web_prototype import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^test/$', views.test, name='test'),
    url(r'^how_it_works/$', views.how_it_works, name='how_it_works'),
    url(r'^materials/$', views.materials, name='materials'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^login/$', views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),


    url(r'^prototype/$', views.index_prototype, name='index_prototype'),
    url(r'^paternity/$', views.paternity, name='paternity'),
    url(r'^parental/$', views.parental, name='parental'),
    url(r'^offspring/$', views.offspring, name='offspring'),
    url(r'^grandparent/$', views.grandparent, name='grandparent'),
)

