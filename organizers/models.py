from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Organizer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="organizer")
    id_type = models.CharField(max_length=254, blank=False)
    personal_identification = models.CharField(max_length=254, blank=False)
    phone = models.CharField(max_length=254, blank=False)
    country = models.CharField(max_length=254, blank=False)
    sector = models.CharField(max_length=30, blank=False)
    organization = models.CharField(max_length=254, blank=False)
    organization_position = models.CharField(max_length=254, blank=False)
    organization_email = models.EmailField(max_length=254, blank=False)
    organization_phone = models.CharField(max_length=254, blank=False)
    status = models.BooleanField(default=False, verbose_name="accepted as organizer")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ["-created_date"]

        db_table = "Poll Organizers"

    def __str__(self) -> str:
        
        return self.first_name
