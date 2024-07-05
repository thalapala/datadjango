from django.urls import path 
from . import views
from django.contrib.auth import views as auth_view
from django.views.generic import TemplateView

urlpatterns = [
    
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('page/', views.page, name='page'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_view.LoginView.as_view(template_name='regapp/login.html'), name="login"),
    path("logout/", TemplateView.as_view(template_name="regapp/logout.html"), name="logout"),
    #path('logout/', views.logout_view, name="logout"),
]