from django.urls import path
from . import views

urlpatterns = [
    path("", views.default, name="default"),
    path("home/<int:id>", views.home, name="home"),
]



    