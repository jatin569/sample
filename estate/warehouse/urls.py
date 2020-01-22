from django.conf.urls import url,include
from . import views
urlpatterns = [
  url(r'^$', views.index,name="index1"),
  url(r'^about$', views.about,name="about1"),
  url(r'^contact$', views.contact,name="contact1"),
  url(r'^elements$', views.elements,name="elements1"),
  url(r'^main$', views.main,name="main1"),
  url(r'^Property$', views.Property,name="Property1"),
  url(r'^property_details$', views.property_details,name="property_details1"),
  url(r'^single_blog$', views.single_blog,name="single_blog1"),
  url(r'^blog$', views.blog,name="blog1"),
  url(r'^login/$', views.login, name='login1'),
  url(r'^logout/$', views.logout, name='logout1'),
    ]