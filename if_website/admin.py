from django.contrib import admin
from if_website.models import Unterzeichner


class UnterzeichnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'wohnort', 'published', 'date_added')
    list_filter = ('published',)

admin.site.register(Unterzeichner, UnterzeichnerAdmin)