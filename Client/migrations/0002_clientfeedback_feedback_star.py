# Generated by Django 3.2 on 2021-08-13 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientfeedback',
            name='Feedback_Star',
            field=models.CharField(choices=[('1', '1 star'), ('2', '2 star'), ('3', '3 star'), ('4', '4 star'), ('5', '5 star')], default=0, max_length=1),
        ),
    ]
