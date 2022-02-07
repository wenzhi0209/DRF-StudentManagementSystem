from django.shortcuts import render
from .models import Certificate
# Create your views here.
from rest_framework import serializers,viewsets

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Certificate
        fields=('id','name','description','created_at','updated_at')
       
class CertificateViewSet(viewsets.ModelViewSet):
    queryset=Certificate.objects.all()
    serializer_class=CertificateSerializer