from django.urls import path
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index),
    path("movies", views.movies),
    path("about", views.about),
    path("gallery", views.gallery),
    path("camera", views.exx),
    path("plate", views.plate),
    path("platedenemeA", views.platedenemeA),
    path("list", views.list),
    path("camera_birlestirme", views.camera_birlestirme),
    path("communication", views.communication),
    path("login", views.login_request),
    path("choose", views.choose),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("adminindex", views.adminindex),
    #path("plate", views.blogs_by_category),
    path('video_feed/', views.video_feed, name='video_feed'),
    path("statistics", views.statistics),
     path("exx", views.exx),
    path("movies/<slug:slug>", views.movie_details)    
]

