from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

from .models import Service

class AdminService(SummernoteModelAdmin):
    list_display = [
        'Title',
        'Category'
    ]
    summernote_fields = ('Description',)
    prepopulated_fields = {'slug': ['Title', ]}


admin.site.register(Service,AdminService)

