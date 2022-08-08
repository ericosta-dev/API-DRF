from django.urls import path

from .views import CourseAPIView,CoursesAPIView,AvaliationAPIView,AvaliationsAPIView

urlpatterns = [
    path('courses/', CoursesAPIView.as_view(), name='courses'),
    path('courses/<int:pk>', CourseAPIView.as_view(), name='course'),
    path('avaliations/', AvaliationsAPIView.as_view(),name='avaliations'),
    path('avaliations/<int:pk>', AvaliationAPIView.as_view(), name='avaliation'),
]