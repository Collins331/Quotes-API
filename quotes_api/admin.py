from django.contrib import admin
from . models import Quote
# Register your models here.

class QuoteAdmin(admin.ModelAdmin):
    list_display = ("author", "description", "created",)

admin.site.register(Quote, QuoteAdmin)