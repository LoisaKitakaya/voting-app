from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name="organizers-dashboard"),
    path('create_poll/', views.create_poll, name="create-poll"),
    path('register_candidate', views.register_candidate, name="register-candidate"),
]