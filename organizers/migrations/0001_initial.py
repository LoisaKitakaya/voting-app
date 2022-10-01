# Generated by Django 4.1.1 on 2022-09-30 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_type', models.CharField(max_length=254)),
                ('personal_identification', models.CharField(max_length=254)),
                ('phone', models.CharField(max_length=254)),
                ('country', models.CharField(max_length=254)),
                ('sector', models.CharField(max_length=30)),
                ('organization', models.CharField(max_length=254)),
                ('organization_position', models.CharField(max_length=254)),
                ('organization_email', models.EmailField(max_length=254)),
                ('organization_phone', models.CharField(max_length=254)),
                ('status', models.BooleanField(default=False, verbose_name='accepted as organizer')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='organizer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Poll Organizers',
                'ordering': ['-created_date'],
            },
        ),
    ]
