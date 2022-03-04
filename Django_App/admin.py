from dataclasses import field
from django.contrib import admin

from .models import Question 

# Register your models here.

class QuestionAdmin(admin. ModelAdmin):
    fields = [
            "title",
            "description",
        ]

admin.site.register(Question)
