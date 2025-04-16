from django.db import models
from django.contrib.auth.models import User

class TextPost(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]  # Display first 50 chars

