# Generated by Django 4.2.9 on 2024-01-26 13:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Scholarshipapp', '0002_scholarship_category_scholarship_item_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholarship_item',
            name='description',
            field=models.CharField(default=django.utils.timezone.now, max_length=350),
            preserve_default=False,
        ),
    ]
