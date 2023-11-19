from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.accept,name="data"),
    path("<int:id>/",views.resume,name="resume"),
]
