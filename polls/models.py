from django.db import models
from organizers.models import Organizer
from candidates.models import Candidate

# Create your models here.
class Poll(models.Model):

    seat = models.CharField(max_length=254, blank=False)
    intro = models.TextField()
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    candidate = models.ManyToManyField(Candidate)
    begin_date = models.DateField()
    end_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ["-created_date"]

        db_table = "Polls Table"

    def __str__(self) -> str:
        
        return self.seat
