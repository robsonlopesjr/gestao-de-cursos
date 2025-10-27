from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE

from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "original_price", "discounted_price")
    search_fields = ("name",)
    name = "courses"
    verbose_name = "cursos"
    formfield_overrides = {models.TextField: {"widget": TinyMCE()}}
