from django.contrib import admin
from .models import Card

class CardAdmin(admin.ModelAdmin):

    list_display = ['phrase', 'created_at', 'updated_at']
    search_fields = ['phrase', 'kanji', 'slug']

admin.site.register(Card, CardAdmin)
