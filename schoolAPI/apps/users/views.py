
from rest_framework import serializers, viewsets
from django.contrib.auth import get_user_model
from .models import UserProfile

# Create your views here.


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    profiles = UserProfileSerializer(read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password','is_student','profiles')
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8}
        }

    def create(self, validated_data):
        # return get_user_model().objects.create_user(**validated_data)
        # is_student is a custom field in the User model so the field only can saved AFTER the User is saved
        is_student = validated_data.pop('is_student')
        user = get_user_model().objects.create_user(**validated_data)
        user.is_student = is_student
        user.save()
        return user


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset=UserProfile.objects.all()
    serializer_class=UserProfileSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
