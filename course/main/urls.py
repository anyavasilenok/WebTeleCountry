from django.urls import path
from . import views
from .django_functions import cost_living

urlpatterns = [
    path("", views.start_page, name="start_page"),
    path("test_page", cost_living.test_function, name="test_page")
]