from django.urls import path
from . import views

urlpatterns = [
    path("stream/", views.stream_view, name="stream"),
]