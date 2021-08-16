from django.db import models

# Create your models here.
class ClientLogo(models.Model):
    Name = models.CharField(max_length=50)
    Image = models.ImageField(upload_to='Startup/ClientLogo')

class ClientFeedback(models.Model):
    Client_Name = models.CharField(max_length=50)
    Company = models.CharField(max_length=50)
    Possition = models.CharField(max_length=50)
    Client_Image = models.ImageField(upload_to='Startup/Client')
    METADATA_FIELD = (
        ('1', '1 star'),
        ('2', '2 star'),
        ('3', '3 star'),
        ('4', '4 star'),
        ('5', '5 star'),
    )
    Feedback_Star = models.CharField(max_length=1, choices=METADATA_FIELD, default=5)
    Feedback = models.TextField()
    