from django.urls import path
from . import views


urlpatterns = [

    path(
        "profile/",
        views.profile,
        name="profile"
    ),

    path(
        "download-result/",
        views.download_result,
        name="download_result"
    ),

]