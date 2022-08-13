from django.urls import path

from rest_framework.routers import SimpleRouter


from .views import (CourseAPIView,
                    CoursesAPIView,
                    AvaliationAPIView,
                    AvaliationsAPIView,
                    CourseViewSet,
                    AvaliationViewSet)


router = SimpleRouter()
router.register('courses',CourseViewSet)
router.register('avaliations',AvaliationViewSet)

urlpatterns = [
    path('courses/', CoursesAPIView.as_view(), name='courses'),
    path('courses/<int:pk>', CourseAPIView.as_view(), name='course'),
    path('courses/<int:course_pk>/avaliations/', AvaliationsAPIView.as_view(), name='course_avaliations'),
    path('courses/<int:course_pk>/avaliations/<int:avaliation_pk>', AvaliationAPIView.as_view(), name='course_avaliation'),
    path('avaliations/', AvaliationsAPIView.as_view(),name='avaliations'),
    path('avaliations/<int:avaliation_pk>', AvaliationAPIView.as_view(), name='avaliation'),

]