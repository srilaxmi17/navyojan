# Generated by Django 5.0.6 on 2024-06-27 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0003_education_all_scholarship'),
    ]

    operations = [
        migrations.DeleteModel(
            name='All_Scholarship',
        ),
        migrations.DeleteModel(
            name='Education',
        ),
    ]
