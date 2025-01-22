from rest_framework import serializers
from .models import Snippet, Comment

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'language', 'tags', 'created_at', 'updated_at', 'version']

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    snippet = serializers.ReadOnlyField(source='snippet.id')

    class Meta:
        model = Comment
        fields = ['id', 'snippet', 'author', 'text', 'created_at']
        