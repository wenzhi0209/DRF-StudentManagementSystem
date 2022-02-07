from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Lecture
# Create your views here.
from rest_framework import serializers,viewsets

class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lecture
        fields=('id','title','description','lecturer_name','date','duration','slides_url','is_required')
       
class LectureViewSet(viewsets.ModelViewSet):
    queryset=Lecture.objects.all()
    serializer_class=LectureSerializer