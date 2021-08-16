from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Project,Category
# Register your models here.

admin.site.register(Category)

class AdminProject(SummernoteModelAdmin):
    list_display = [
        'Client',
        'ProjectName',
    ]
    prepopulated_fields = {'slug': ['Title', ]}
    summernote_fields = ('Description')


admin.site.register(Project,AdminProject)