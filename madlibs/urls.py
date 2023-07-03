from django.contrib import admin
from django.urls import path
from django.urls import include

app_name = "madlibs"
urlpatterns = [
    path('admin/', admin.site.urls),
    path("madlibs/", include("madlibsapp.urls"))
]
