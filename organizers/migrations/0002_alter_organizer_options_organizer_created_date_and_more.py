# Generated by Django 4.1.1 on 2022-09-28 12:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('organizers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organizer',
            options={'ordering': ['-created_date']},
        ),
        migrations.AddField(
            model_name='organizer',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organizer',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterModelTable(
            name='organizer',
            table='Poll Organizers',
        ),
    ]
