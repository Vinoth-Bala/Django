# Generated by Django 5.0.1 on 2024-02-13 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Serialize', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='dept',
            new_name='dept_id',
        ),
    ]
