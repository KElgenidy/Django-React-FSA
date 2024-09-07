from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Notes

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        """
        Defines the serializer for the User model, which is used to handle user data in the API.
        
        The `UserSerializer` class inherits from `serializers.ModelSerializer` and provides the following functionality:
        
        - Specifies the `User` model as the underlying model for the serializer.
        - Defines the fields to be included in the serialized data, which are `id`, `username`, and `password`.
        - Sets the `password` field to be `write_only`, meaning it will be accepted when creating a new user but will not be returned when retrieving user data.
        """
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Creates a new user instance with the provided validated data.
        
        Args:
            validated_data (dict): A dictionary containing the validated user data, such as username and password.
        
        Returns:
            User: The newly created user instance.
        """
        user = User.objects.create_user(**validated_data)
        return user
        
class NoteSerializer(serializers.ModelSerializer): 
    class Meta:
        """
        Defines the serializer for the Notes model, which is used to handle note data in the API.
        
        The `NoteSerializer` class inherits from `serializers.ModelSerializer` and provides the following functionality:
        
        - Specifies the `Notes` model as the underlying model for the serializer.
        - Defines the fields to be included in the serialized data, which are `id`, `title`, `content`, `created_at`, and `author`.
        - Sets the `author` field to be `read_only`, read who the author is, but user will not be able to change it. (backend will handle this)
        """
        model = Notes
        fields = ('id', 'title', 'content', 'created_at', 'author')
        extra_kwargs = {'author': {'read_only': True}}
