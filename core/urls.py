from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home-page"),
    path('register_organizer/', views.register_organizer, name="register-organizer"),
    path('register_voter/', views.register_voter, name="register-voter"),
    path('login_organizer/', views.login_organizer, name="login-organizer"),
    path('login_voter/', views.login_voter, name="login-voter"),
]