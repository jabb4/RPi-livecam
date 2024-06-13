from django.urls import path
from . import views

urlpatterns = [
    path("", views.stream_view, name="stream"),
    path("saved/", views.saved_series_view, name="saved"),
]