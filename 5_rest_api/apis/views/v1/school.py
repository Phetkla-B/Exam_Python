from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from ...models import School
from ...serializers import SchoolSerializer
from ...filters import SchoolFilter

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SchoolFilter