from django.db import models
from django.shortcuts import reverse
# Create your models here.
class Service(models.Model):
    Category = models.CharField(max_length=80, unique=True)
    Title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    ShortDes = models.CharField(max_length=250)
    ServiceImage = models.ImageField(upload_to='Startup/Service')
    Service_Hover_Image = models.ImageField(upload_to='Startup/Service')
    Service_Details_Image = models.ImageField(upload_to='Startup/Service', blank = True, null = True)
    Description = models.TextField()

    def get_absolute_url(self):
        return reverse('Services:ServiceList', kwargs={'slug': self.slug})
    