from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactForm
from .models import About, Course


def home(request):
    courses = Course.objects.filter(situation=True).order_by("-id")
    return render(request, "courses/home.html", {"courses": courses})


def course(request, slug):
    courses = Course.objects.filter(situation=True).order_by("-id")[:3]
    course = get_object_or_404(Course, slug=slug)
    return render(
        request, "courses/course.html", {"course": course, "courses": courses}
    )


def about(request):
    abouts = About.objects.filter(situation=True).order_by("-id")
    return render(request, "courses/about.html", {"abouts": abouts})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mensagem enviada com sucesso!")
            return redirect("contact")
        else:
            messages.error(
                request,
                "Erro ao enviar a mensagem. \
                    Verifique os dados e tente novamente.",
            )
    else:
        form = ContactForm()

    return render(request, "courses/contact.html", {"form": form})
