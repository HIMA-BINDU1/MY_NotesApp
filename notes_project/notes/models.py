from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_pinned = models.BooleanField(default=False)  # New field to track pinned notes

    def __str__(self):
        return self.title

