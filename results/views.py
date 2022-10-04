from django.shortcuts import render
from polls.models import Poll
from candidates.models import Candidate
from django.contrib.auth.models import User
from voters.models import Voter
from votes.models import Vote

# Create your views here.
def poll_results(request, id):

    poll = Poll.objects.get(id=id)

    total_poll_votes = len(Vote.objects.filter(poll=poll))

    all_poll_candidates = Candidate.objects.filter(poll=poll)

    candidate_results = []

    for candidate in all_poll_candidates:

        result = {
            'candidate': f'{candidate.first_name} {candidate.last_name}',
            'image': candidate.image.url,
            'total': len(Vote.objects.filter(candidate=candidate)),
        }

        candidate_results.append(result)

    print(candidate_results)

    context = {
        'poll_votes': total_poll_votes,
        'candidate_votes': candidate_results,
    }

    return render(request, 'results/poll_results.html', context)