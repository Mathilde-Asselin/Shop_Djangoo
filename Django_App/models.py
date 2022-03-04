from django.db import models

# Create your models here.

class Question(models.Model) :
    title = models.CharField(max_length = 200)
    description = models.TextField(default='')
    def __str__(self):
        return self.title


