from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .models import Organizer
from polls.models import Poll
from candidates.models import Candidate
from django.contrib import messages

# Create your views here.
@permission_required('polls.add_poll', raise_exception=True)
def dashboard(request):

    user = request.user

    organizer = Organizer.objects.filter(user=user).first()

    organizer_polls = Poll.objects.filter(organizer=organizer)

    context = {
        'all_polls': organizer_polls,
    }

    return render(request, 'organizers/dashboard.html', context)

def create_poll(request):

    if request.method == 'POST':

        user = request.user

        organizer = Organizer.objects.filter(user=user).first()

        seat = request.POST['seat']
        intro = request.POST['intro']
        organizer = organizer
        begin_date = request.POST['begin_date']
        end_date = request.POST['end_date']

        Poll.objects.create(
            seat=seat,
            intro=intro,
            organizer=organizer,
            begin_date=begin_date,
            end_date=end_date
        )

        messages.success(request, 'Poll has been created successfully.')

    return render(request, 'organizers/dashboard.html')

def register_candidate(request):

    if request.method == 'POST':

        user = request.user

        organizer = Organizer.objects.filter(user=user).first()

        organizer = organizer
        poll_id = request.POST['poll_id']
        poll = Poll.objects.get(id=poll_id)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        id_type = request.POST['id_type']
        personal_identification = request.POST['personal_id']
        image = request.FILES['image']
        country = request.POST['country']
        organization = request.POST['organization']

        Candidate.objects.create(
            organizer=organizer,
            poll=poll,
            first_name=first_name,
            last_name=last_name,
            email=email,
            id_type=id_type,
            personal_identification=personal_identification,
            image=image,
            country=country,
            organization=organization
        )

        # print(f'{organizer}, {poll}, {image}')

        messages.success(request, 'Candidate has been registered successfully.')

    return render(request, 'organizers/dashboard.html')
