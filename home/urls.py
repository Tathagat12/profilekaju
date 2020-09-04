from django.contrib import admin
from django.urls import path,include
from home import views



admin.site.site_header ="Login to Developer Tathagat"
admin.site.site_title ="Wellcome to Tathagat's Dashboard"
admin.site.index_title ="Wellcome to this Portal"
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
   
] 