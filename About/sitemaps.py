from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from Blog.models import Blogpost
from Projects.models import Project
from Services.models import Service

class StaticViewSitemap(Sitemap):

    def items(self):
        return [
            'Home:Home',
            'Contact:Contact',
            'About:About',
            'About:FAQ',
            'Blog:Blog',
            'Services:Services',
            'Projects:Project',
        ]
    
    def location(self,item):
        return reverse(item)


class BlogpostSitemap(Sitemap):

    def items(self):
        return Blogpost.objects.all()


class ProjectSitemap(Sitemap):

    def items(self):
        return Project.objects.all()

class ServiceSitemap(Sitemap):

    def items(self):
        return Service.objects.all()

