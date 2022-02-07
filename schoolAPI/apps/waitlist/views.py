from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import WaitlistEntry
# Create your views here.
from rest_framework import serializers,viewsets

class WaitlistEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model=WaitlistEntry
        fields='__all__'
       
class WaitlistEntryViewSet(viewsets.ModelViewSet):
    queryset=WaitlistEntry.objects.all()
    serializer_class=WaitlistEntrySerializer