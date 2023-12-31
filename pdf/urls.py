from django.contrib.auth import views as auth_view
from django.contrib import admin
from django.urls import path
from . import views

app_name="cv"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path("generate/",views.accept,name="data"),
    path("<int:id>/",views.resume,name="resume"),
    path("list/",views.get_list,name="data_list"),
    path("del/<int:id>/",views.delete_data,name="delete"),
    path("view/<int:id>/",views.view_cv,name="view"),
    path('edit_profile/<int:id>/', views.edit_profile, name='edit_profile'),
    path('signup/',views.Register,name="signup"),
    path('login/',auth_view.LoginView.as_view(template_name='pdf/login.html'),name='login'),
     path('logout/',auth_view.LogoutView.as_view(template_name='pdf/logout.html'),name='logout'),
]
