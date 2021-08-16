from django.contrib import admin

from .models import SocialLink,TeamMember,About

# Register your models here.

admin.site.register(About)
admin.site.register(TeamMember)
admin.site.register(SocialLink)

