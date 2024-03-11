from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    '''Admin View for Profile)'''

    list_display = ('user',  'name', 'email', 'location',  )