from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("course/<slug:slug>/", views.course, name="course"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
]
