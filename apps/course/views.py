from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view



from .models import Course,Avaliation
from .serializers import CourseSerializer,AvaliationSerializer


class CourseAPIView(APIView):

    def get(self,request):
        print(request) 
        courses= Course.objects.all()
        serializer = CourseSerializer(courses, many = True)
        return Response(serializer.data)


class AvaliationAPIView(APIView):
    """
        API Avaliation
    """

    def get(self, request):
        avaliations = Avaliation.objects.all()
        serializer = AvaliationSerializer(avaliations, many=True)
        return Response(serializer.data)


