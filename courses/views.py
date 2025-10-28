from django.shortcuts import render


def home(request):
    return render(request, "courses/home.html")


def about(request):
    return render(request, "courses/about.html")


def contact(request):
    return render(request, "courses/contact.html")
