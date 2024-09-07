from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    """
    Represents a note in the application. Each note has a title, content, creation timestamp, and is associated with a specific user.
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return self.title
