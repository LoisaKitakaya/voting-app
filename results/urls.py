from django.urls import path
from . import views

urlpatterns = [
    path('poll_results/<int:id>/', views.poll_results, name="poll-results"),
]