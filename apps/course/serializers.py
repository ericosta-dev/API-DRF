from rest_framework import serializers

from .models import Course,Avaliation


class AvaliationSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email':{'write_only' : True}
        }
        model = Avaliation
        fields = (
            'id',
            'course',
            'name',
            'email',
            'comment',
            'avaliation',
            'publication',
            'active'
        )


class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'url',
            'publication',
            'active'
        )
