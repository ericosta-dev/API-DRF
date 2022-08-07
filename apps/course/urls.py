from django.urls import path

from .views import CourseAPIView,AvaliationAPIView

urlpatterns = [
    path('course/', CourseAPIView.as_view(), name='course'),
    path('avaliation/', AvaliationAPIView.as_view(),name='avaliations')
]