from django.contrib import admin
from .models import WhatsAppMessage

# Register your models here.

#Admin interface for WhatsAppMessage model
@admin.register(WhatsAppMessage)
class WhatsAppMessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'status', 'timestamp')
    list_filter = ('status', 'timestamp')
    search_fields = ('sender', 'receiver', 'content')
