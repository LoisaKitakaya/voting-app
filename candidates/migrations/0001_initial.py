# Generated by Django 4.1.1 on 2022-09-30 03:07

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizers', '0004_organizer_organization_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254)),
                ('last_name', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('personal_identification', models.CharField(max_length=254)),
                ('photo', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('country', models.CharField(max_length=254)),
                ('organization', models.CharField(max_length=254)),
                ('vying_position', models.CharField(max_length=254)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizers.organizer')),
            ],
            options={
                'db_table': 'Poll Candidates',
                'ordering': ['-created_date'],
            },
        ),
    ]
