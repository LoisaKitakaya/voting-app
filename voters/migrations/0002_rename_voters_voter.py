# Generated by Django 4.1.1 on 2022-09-28 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voters', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Voters',
            new_name='Voter',
        ),
    ]
