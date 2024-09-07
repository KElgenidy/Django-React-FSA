from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Notes

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    """
    Allows unauthenticated users to create a new user account.
    
    This view provides an API endpoint for creating a new user account. It uses the `UserSerializer` to handle the serialization and deserialization of the user data. The `AllowAny` permission class is used to allow unauthenticated access to this endpoint.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class NoteListCreate(generics.ListCreateAPIView):
    """
    Provides an API endpoint for listing and creating notes. Only authenticated users can access this view.
    
    The `NoteListCreate` class is a Django REST Framework `ListCreateAPIView` that handles the listing and creation of notes. It uses the `NoteSerializer` to handle the serialization and deserialization of the note data.
    
    The `get_queryset` method filters the notes to only include those created by the currently authenticated user.
    
    The `perform_create` method saves the new note, setting the `author` field to the currently authenticated user.
    """
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user # Get the currently authenticated user
        return Notes.objects.filter(author=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)


class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user # Get the currently authenticated user
        return Notes.objects.filter(author=user)
    
    
    

