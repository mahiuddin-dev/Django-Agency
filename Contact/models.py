from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=250)
    phone = models.CharField(max_length=50)
    subject = models.CharField(max_length=250)
    msg = models.TextField()

    def __str__(self):
        return self.subject + ' by ' + self.name

