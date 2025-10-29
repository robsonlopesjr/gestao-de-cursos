from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# Carregando página 404 personalizada
handler404 = "app.views.custom_page_not_found"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("courses.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
