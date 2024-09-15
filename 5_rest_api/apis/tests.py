from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import School, Classroom, Teacher, Student
from django.urls import reverse

# Create your tests here.

class APITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

        # สร้างข้อมูลเริ่มต้นสำหรับการทดสอบ
        self.school = School.objects.create(
            name="Test School", abbreviation="TS", address="123 Test Street"
        )
        self.classroom = Classroom.objects.create(
            year=1, section="A", school=self.school
        )
        self.teacher = Teacher.objects.create(
            first_name="John", last_name="Doe", gender="Male"
        )
        self.teacher.classrooms.add(self.classroom)
        self.student = Student.objects.create(
            first_name="Jane", last_name="Smith", gender="Female", classroom=self.classroom
        )

    ### School Tests ###
    def test_create_school(self):
        url = reverse('school-list')
        data = {'name': 'New School', 'abbreviation': 'NS', 'address': '456 New Avenue'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(School.objects.count(), 2)

    def test_get_school_list(self):
        url = reverse('school-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_school_by_name(self):
        url = reverse('school-list')
        response = self.client.get(url, {'name': 'Test School'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_school_detail(self):
        url = reverse('school-detail', args=[self.school.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['classroom_count'], 1)
        self.assertEqual(response.data['teacher_count'], 1)
        self.assertEqual(response.data['student_count'], 1)

    def test_update_school(self):
        url = reverse('school-detail', args=[self.school.id])
        data = {'name': 'Updated School Name'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.school.refresh_from_db()
        self.assertEqual(self.school.name, 'Updated School Name')

    def test_delete_school(self):
        url = reverse('school-detail', args=[self.school.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(School.objects.count(), 0)

    ### Classroom Tests ###
    def test_create_classroom(self):
        url = reverse('classroom-list')
        data = {'year': 2, 'section': 'B', 'school': self.school.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Classroom.objects.count(), 2)

    def test_get_classroom_list(self):
        url = reverse('classroom-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_classroom_by_school(self):
        url = reverse('classroom-list')
        response = self.client.get(url, {'school': self.school.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_classroom_detail(self):
        url = reverse('classroom-detail', args=[self.classroom.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['teachers']), 1)
        self.assertEqual(len(response.data['students']), 1)

    def test_update_classroom(self):
        url = reverse('classroom-detail', args=[self.classroom.id])
        data = {'section': 'C'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.classroom.refresh_from_db()
        self.assertEqual(self.classroom.section, 'C')

    def test_delete_classroom(self):
        url = reverse('classroom-detail', args=[self.classroom.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Classroom.objects.count(), 0)

    ### Teacher Tests ###
    def test_create_teacher(self):
        url = reverse('teacher-list')
        data = {'first_name': 'New', 'last_name': 'Teacher', 'gender': 'Male'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Teacher.objects.count(), 2)

    def test_get_teacher_list(self):
        url = reverse('teacher-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_teacher_by_name(self):
        url = reverse('teacher-list')
        response = self.client.get(url, {'first_name': 'John'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_teacher_detail(self):
        url = reverse('teacher-detail', args=[self.teacher.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['classrooms']), 1)

    def test_update_teacher(self):
        url = reverse('teacher-detail', args=[self.teacher.id])
        data = {'last_name': 'Updated'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.teacher.refresh_from_db()
        self.assertEqual(self.teacher.last_name, 'Updated')

    def test_delete_teacher(self):
        url = reverse('teacher-detail', args=[self.teacher.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Teacher.objects.count(), 0)

    ### Student Tests ###
    def test_create_student(self):
        url = reverse('student-list')
        data = {'first_name': 'New', 'last_name': 'Student', 'gender': 'Male', 'classroom': self.classroom.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 2)

    def test_get_student_list(self):
        url = reverse('student-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_student_by_name(self):
        url = reverse('student-list')
        response = self.client.get(url, {'first_name': 'Jane'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_student_detail(self):
        url = reverse('student-detail', args=[self.student.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['classroom'], self.classroom.id)

    def test_update_student(self):
        url = reverse('student-detail', args=[self.student.id])
        data = {'last_name': 'Updated'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.student.refresh_from_db()
        self.assertEqual(self.student.last_name, 'Updated')

    def test_delete_student(self):
        url = reverse('student-detail', args=[self.student.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Student.objects.count(), 0)