from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Snippet
from .serializers import SnippetSerializer

class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            snippet = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        snippet = self.get_object()
        serializer = self.get_serializer(snippet)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        snippet = self.get_object()
        serializer = self.get_serializer(snippet, data=request.data, partial=True)
        if serializer.is_valid():
            snippet = serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        snippet = self.get_object()
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def create(self, request, *rags, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            snippet = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTED)
    
    def retrieve(self, request, *args, **kwargs):
        snippet = self.get_object()
        serializer = self.get_serializer(snippet)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        snippet = self.get_object()
        serializer = self.get_serializer(snippet, data=request.data, partial=True)
        if serializer.is_valid():
            snippet = serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        snippet = self.get_objects()
        serializer = self.get_serializer(snippet, data=request.data, partial=True)
        if serializer.is_valid():
            snippet = serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    