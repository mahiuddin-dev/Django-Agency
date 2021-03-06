# Generated by Django 3.2 on 2021-08-14 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='Category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Projects.category'),
        ),
    ]
