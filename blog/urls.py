from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("samplepost/", views.samplepost, name="samplepost"),
    path("<int:pid>/", views.detail, name="detail"),
]
