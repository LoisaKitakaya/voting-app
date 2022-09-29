from django.contrib import admin
from .models import Candidate

# Register your models here.
@admin.register(Candidate)
class CandidateAdminView(admin.ModelAdmin):

    model = Candidate

    list_display = (
        'first_name',
        'email',
        'organization',
        'vying_position',
    )

    list_filter = (
        'created_date',
        'updated_date',
    )