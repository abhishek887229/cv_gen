from django.contrib import admin
from django.urls import path
from . import views

app_name="cv"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.accept,name="data"),
    path("<int:id>/",views.resume,name="resume"),
    path("list/",views.get_list,name="data_list"),
]
