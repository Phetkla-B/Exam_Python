from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from apis.views.v1.school import SchoolViewSet
from apis.views.v1.classroom import ClassroomViewSet
from apis.views.v1.teacher import TeacherViewSet
from apis.views.v1.student import StudentViewSet


router = DefaultRouter()

router.register(r'schools', SchoolViewSet, basename='school')
router.register(r'classrooms', ClassroomViewSet, basename='classroom')
router.register(r'teachers', TeacherViewSet, basename='teacher')
router.register(r'students', StudentViewSet, basename='student')

api_v1_urls = (router.urls, 'api-v1')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include((router.urls, 'api-v1')))
]
