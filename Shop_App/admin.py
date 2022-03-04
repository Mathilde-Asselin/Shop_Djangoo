from dataclasses import field
from django.contrib import admin

from .models import Card 

# Register your models here.

class CardAdmin(admin. ModelAdmin):
    fields = [
            "title",
            "img",
            "description",
            "price",
            "quantity",
        ]

admin.site.register(Card)


