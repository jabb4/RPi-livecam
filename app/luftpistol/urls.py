from django.urls import path
from . import views

urlpatterns = [
    path("live/", views.stream_view, name="stream"),
    path("serier/", views.saved_series_view, name="saved"),
]