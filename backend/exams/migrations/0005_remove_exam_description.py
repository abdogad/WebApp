# Generated by Django 5.0.6 on 2024-06-19 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0004_rename_response_responses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='description',
        ),
    ]
