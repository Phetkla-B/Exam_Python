from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from ...models import Student
from ...serializers import StudentSerializer
from ...filters import StudentFilter

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StudentFilter
