# Generated by Django 3.2 on 2021-08-13 17:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_rename_slug_blogpost_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='Image_For_Detail',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='Startup/Blog'),
            preserve_default=False,
        ),
    ]