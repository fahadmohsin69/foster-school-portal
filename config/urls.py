from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

path("", include("accounts.urls")),
path("admin/", admin.site.urls),
path("dashboard/", include("core.urls")),
path("students/", include("students.urls")),
# path("results/", include("results.urls")),
]


urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)