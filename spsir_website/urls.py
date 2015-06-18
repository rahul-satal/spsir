from django.conf.urls import patterns, url

from spsir_website import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^spsir_website/cv/$', views.cv, name='cv'),
    url(r'^spsir_website/education/$', views.education, name='education'),
    url(r'^spsir_website/Miscellaneous/$', views.Miscellaneous, name='Miscellaneous'),
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
    
    url(r'^spsir_website/research/project/$', views.project, name='project'),
    url(r'^spsir_website/teaching/sem_project/$', views.sem_project, name='sem_project'),
    url(r'^spsir_website/teaching/dna/$', views.dna, name='dna'),
    url(r'^spsir_website/teaching/cg/$', views.cg, name='cg'),
    url(r'^spsir_website/teaching/r_in_c/$', views.r_in_c, name='r_in_c'),
    url(r'^spsir_website/teaching/ada/$', views.ada, name='ada'),
    url(r'^spsir_website/teaching/dco/$', views.dco, name='dco'),

    url(r'^spsir_website/my_teachers/$', views.my_teachers, name='my_teachers'),

    url(r'^spsir_website/recommendations/$', views.recommendations, name='recommendations'),
    url(r'^spsir_website/recommendations/books/$', views.books, name='books'),
    url(r'^spsir_website/recommendations/ecc/$', views.ecc, name='ecc'),
    

    url(r'^spsir_website/dc_iips/$', views.dc_iips, name='dc_iips'),

    url(r'^spsir_website/miscellaneous/my_students/$', views.my_students, name='my_students'),
    url(r'^spsir_website/miscellaneous/spritual_gurus/$', views.spritual_gurus, name='spritual_gurus'),
    url(r'^spsir_website/miscellaneous/workshop/$', views.workshop, name='workshop'),
    url(r'^spsir_website/miscellaneous/my_friends/$', views.my_friends, name='my_friends'),
                           


      
    
    
  
  
)
