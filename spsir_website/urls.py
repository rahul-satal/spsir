from django.conf.urls import patterns, url

from spsir_website import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
