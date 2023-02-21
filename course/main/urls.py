from django.urls import path
from . import views

urlpatterns = [
    path("", views.start_page, name="start_page"),
    path("test_page", views.test_function, name="test_page")
]