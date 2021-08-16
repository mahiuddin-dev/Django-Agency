from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
from .models import ClientLogo,ClientFeedback

class AdminClientLogo(admin.ModelAdmin):
    list_display = [
        'Name',
        'Image'
    ]
admin.site.register(ClientLogo,AdminClientLogo)


class AdminClientFeedback(admin.ModelAdmin):
    list_display = [
        'Client_Name',
        'Client_Image',
        'Feedback_Star',
    ]

admin.site.register(ClientFeedback,AdminClientFeedback)