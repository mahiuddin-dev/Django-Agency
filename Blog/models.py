from django.db import models
from taggit.managers import TaggableManager
from django.shortcuts import reverse
# Create your models here.

# Blog Post Model
class Blogpost(models.Model):
    Name = models.CharField(max_length=50, default='Md Mahiuddin')
    Title = models.CharField(max_length=250)
    Tags = TaggableManager()
    Image = models.ImageField(upload_to='Startup/Blog')
    Image_For_Detail = models.ImageField(upload_to='Startup/Blog')
    Short_Description = models.TextField(max_length=250)
    Description = models.TextField(max_length=5000)
    Time = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('Blog:BlogDetail', kwargs={'slug': self.slug})

    
# Comment Model
class Comment(models.Model):
    Post = models.ForeignKey(Blogpost, on_delete= models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    email = models.CharField(max_length=150)
    creation = models.DateTimeField(auto_now_add=True)
    approve = models.BooleanField(default=False)
