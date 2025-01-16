from django.db import models
from django.contrib.auth.models import User

class Snippet(models.Model):
    content = models.TextField()
    language = models.CharField(max_length=100)
    tags = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, related_name='snippets', on_delete=models.CASCADE)
    version = models.IntegerField(default=1)
    is_forked = models.BooleanField(default=False)
    parent_snippet = models.ForeignKey('self', null=True, blank=True, related_name='forks', on_delete=models.SET_NULL)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return f'Snippet by {self.owner.username} - {self.language}'