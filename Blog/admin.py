from django.contrib import admin
from django.contrib.admin.decorators import register
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

from .models import Blogpost,Comment

class AdminPost(SummernoteModelAdmin):
    list_display = [
        'Name',
        'Title',
    ]
    summernote_fields = ('Description',)
    prepopulated_fields = {'slug': ['Title', ]}

admin.site.register(Blogpost, AdminPost)

class Adminomment(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
    ]
admin.site.register(Comment, Adminomment)
