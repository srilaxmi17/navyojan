# Generated by Django 5.0.2 on 2024-06-03 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Scholarshipapp', '0017_upcoming_scholarship_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholarship_details',
            name='Dead_line',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='scholarship_details',
            name='Published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
