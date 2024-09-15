from django.db import models
from django.conf import settings

# Create your models here.
#School detail
class School(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=10)
    address = models.TextField()

    def __str__(self):
        return self.name
    
#Classroom detail
class Classroom(models.Model):
    year = models.PositiveIntegerField()
    section = models.CharField(max_length=10)
    school = models.ForeignKey(School, related_name='classrooms', on_delete=models.CASCADE, default=settings.DEFAULT_SCHOOL_ID)
    
    def __str__(self):
        return f"{self.year} {self.section}"
    
#Teacher detail
class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    classrooms = models.ManyToManyField(Classroom, related_name='teachers')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

#Student detail
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    classroom = models.ForeignKey(Classroom, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"