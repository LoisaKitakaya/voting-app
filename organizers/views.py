from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from django.contrib import messages

# Create your views here.
@permission_required('polls.add_poll', raise_exception=True)
def dashboard(request):

    return render(request, 'organizers/dashboard.html')