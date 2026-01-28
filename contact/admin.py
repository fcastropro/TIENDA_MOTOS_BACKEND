from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject', 'city', 'phone', 'created_at')
    search_fields = ('name', 'email', 'subject', 'city', 'phone')
    list_filter = ('created_at',)
