import django_filters
from .models import School, Classroom, Teacher, Student

# code here

class SchoolFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = School
        fields = ['name']

class ClassroomFilter(django_filters.FilterSet):
    school = django_filters.ModelChoiceFilter(queryset=School.objects.all())

    class Meta:
        model = Classroom
        fields = ['school']

class TeacherFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    gender = django_filters.ChoiceFilter(choices=[('Male', 'Male'), ('Female', 'Female')])
    classroom = django_filters.ModelChoiceFilter(queryset=Classroom.objects.all())

    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'gender', 'classrooms']

class StudentFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    gender = django_filters.ChoiceFilter(choices=[('Male', 'Male'), ('Female', 'Female')])
    classroom = django_filters.ModelChoiceFilter(queryset=Classroom.objects.all())

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'gender', 'classroom']