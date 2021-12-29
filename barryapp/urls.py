from django.contrib import admin
from django.urls import path
from barryapp import views

urlpatterns = [
    path("", views.index, name= 'barryapp'),
    path("booknow", views.booknow, name= "booknow"),
    path("about", views.about, name= 'about'),
    path("applynow", views.applynow, name= 'applynow'),
    path("musicalbum", views.musicalbum, name= 'musicalbum'),
    path("$", views.contact, name='contact us'),
    path("payment", views.payment, name='payment'),
    path("success", views.success, name='success'),
    path("standard", views.standard, name='standard'),
    path("professional", views.professional, name='professional'),
    path("advance", views.advance, name='Advance'),
    path("paytm", views.paytm, name='paytm'),


  
]
