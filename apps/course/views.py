from rest_framework import generics

from .models import Course, Avaliation
from .serializers import CourseSerializer,AvaliationSerializer

class CoursesAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class AvaliationsAPIView(generics.ListCreateAPIView):
    queryset = Avaliation.objects.all()
    serializer_class = AvaliationSerializer


class AvaliationAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliation.objects.all()
    serializer_class = AvaliationSerializer