from django.contrib import admin

from .models import UserProfile, PoliticalParty

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(PoliticalParty)
