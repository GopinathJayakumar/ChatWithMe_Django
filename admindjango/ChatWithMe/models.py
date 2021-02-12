from django.db import models


# Create your models here.

class Chat(models.Model):
    user = models.CharField(max_length=140)
    content = models.CharField(max_length=140)
    timestamp = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
