from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Project(models.Model):
    ProjectName = models.CharField(max_length=50)
    Title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Client = models.CharField(max_length=50)
    Image = models.ImageField(upload_to='Startup/Project')
    Description = models.TextField()

    def get_absolute_url(self):
        return reverse('Projects:ProjectDetail', kwargs={'slug': self.slug})

