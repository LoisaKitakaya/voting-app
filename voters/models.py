from django.db import models

# Create your models here.
class Voter(models.Model):

    first_name = models.CharField(max_length=254, blank=False)
    last_name = models.CharField(max_length=254, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    personal_identification = models.CharField(max_length=254, blank=False)
    country = models.CharField(max_length=254, blank=False)
    organization = models.CharField(max_length=254, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ["-created_date"]

        db_table = "Poll Voters"

    def __str__(self) -> str:
        
        return self.first_name