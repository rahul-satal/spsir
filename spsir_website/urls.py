from django.conf.urls import patterns, url

from spsir_website import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^spsir_website/cv/$', views.cv, name='cv'),
    url(r'^spsir_website/education/$', views.education, name='education'),
    url(r'^spsir_website/memberships/$', views.memberships, name='memberships'),
    url(r'^spsir_website/research/$', views.research, name='research'),
    url(r'^spsir_website/teaching/$', views.teaching, name='teaching'),
    url(r'^spsir_website/contactMe/$', views.contactMe, name='contactMe'),
    url(r'^spsir_website/header/$', views.header, name='header'),
    url(r'^spsir_website/footer/$', views.footer, name='footer'),
    url(r'^spsir_website/research/publications/$', views.publications, name='publications'),
    url(r'^spsir_website/subjectsThought/$', views.subjectsThought, name='subjectsThought'),
    url(r'^spsir_website/InternationalConferences/$', views.InternationalConferences, name='InternationalConferences'),
    url(r'^spsir_website/journalPublications/$', views.journalPublications, name='journalPublications'),
    url(r'^spsir_website/nationalConferences/$', views.nationalConferences, name='nationalConferences'),
    url(r'^spsir_website/profile/$', views.profile, name='profile'),
    url(r'^spsir_website/footer/$', views.footer, name='footer'),
    url(r'^spsir_website/footer/$', views.footer, name='footer'),
    url(r'^spsir_website/footer/$', views.footer, name='footer'),
    url(r'^spsir_website/footer/$', views.footer, name='footer'),
    url(r'^spsir_website/footer/$', views.footer, name='footer'),
    

    
    
  
  
)
