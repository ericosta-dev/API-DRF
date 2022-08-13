from rest_framework import generics
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response 
from rest_framework import mixins


from .models import Course, Avaliation
from .serializers import CourseSerializer,AvaliationSerializer

"""
API V1
"""

class CoursesAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class AvaliationsAPIView(generics.ListCreateAPIView):
    queryset = Avaliation.objects.all()
    serializer_class = AvaliationSerializer

    def get_queryset(self):
        if self.kwargs.get('course_pk'):
            return self.queryset.filter(course_id=self.kwargs.get('course_pk'))
        return self.queryset.all()

class AvaliationAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliation.objects.all()
    serializer_class = AvaliationSerializer

    def get_object(self):
        if self.kwargs.get('course_pk'):
            return get_object_or_404(self.get_queryset(),
                                    course_id=self.kwargs.get('course_pk'),
                                    pk=self.kwargs.get('avaliation_pk'))
        return get_object_or_404(self.get_queryset(),pk=self.kwargs.get('avaliation_pk'))


"""
API V2
"""

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['get'])
    def avaliations(self,request, pk=None):
        course = self.get_object()
        serializer = AvaliationSerializer(course.avaliations.all(), many=True)
        return Response(serializer.data)

# class AvaliationViewSet(viewsets.ModelViewSet):
#     queryset = Avaliation.objects.all()
#     serializer_class = AvaliationSerializer

class AvaliationViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):

    queryset = Avaliation.objects.all()
    serializer_class = AvaliationSerializer