# Generated by Django 5.0.1 on 2024-02-01 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='Blood_Group',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='person',
            name='ph_no',
            field=models.IntegerField(default=0),
        ),
    ]
