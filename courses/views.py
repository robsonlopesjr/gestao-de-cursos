from django.shortcuts import get_object_or_404, render

from .models import Course


def home(request):
    courses = Course.objects.filter(situation=True).order_by("-id")
    return render(request, "courses/home.html", {"courses": courses})


def course(request, id):
    course = get_object_or_404(Course, id=id)
    return render(request, "courses/course.html", {"course": course})


def about(request):
    return render(request, "courses/about.html")


def contact(request):
    return render(request, "courses/contact.html")
