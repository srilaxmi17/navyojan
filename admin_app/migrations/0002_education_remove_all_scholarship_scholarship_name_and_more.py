# Generated by Django 5.0.6 on 2024-06-19 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='all_scholarship',
            name='scholarship_name',
        ),
        migrations.AddField(
            model_name='all_scholarship',
            name='All_Scholarship',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
