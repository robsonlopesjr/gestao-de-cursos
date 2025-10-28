from django.shortcuts import render

from .models import Course


def home(request):
    courses = Course.objects.filter(situation=True).order_by("-id")
    return render(request, "courses/home.html", {"courses": courses})


def about(request):
    return render(request, "courses/about.html")


def contact(request):
    return render(request, "courses/contact.html")
