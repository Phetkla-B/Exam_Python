from rest_framework import serializers

# code here
from .models import School, Classroom, Teacher, Student


#model School
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'abbreviation', 'address']

#model Classroom
class ClassroomSerializer(serializers.ModelSerializer):
    school = SchoolSerializer(read_only=True)
    class Meta:
        model = Classroom
        fields = ['id', 'year', 'section', 'school']

#model Teacher
class TeacherSerializer(serializers.ModelSerializer):
    classrooms = ClassroomSerializer(many=True, read_only=True)
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'gender', 'classrooms']

#model Student
class StudentSerializer(serializers.ModelSerializer):
    classroom = ClassroomSerializer(read_only=True)
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'gender', 'classroom']