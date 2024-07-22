from django.shortcuts import render
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student
from .serializers import StudentSerializer
from classes.models import Class
from .serializers import ClassesSerializer
from .serializers import ClassroomPeriodSerializer
from classroom_period.models import ClassroomPeriod
from courses.models import Courses
from .serializers import CoursesSerializer
from teacher.models import Teacher
from .serializers import TeacherSerializer

class StudentListViews(APIView):
    def get(self,request):
        Students = Student.objects.all()
        serializer = StudentSerializer(Students,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status. HTTP_400_BAD_REQUEST)

class ClassRoomListView(APIView):
    def get(self,request):
        Classes = Class.objects.all()
        serializer = ClassesSerializer(Classes,many=True)
        return Response(serializer.data)
    
class ClassroomPeriodListView(APIView):
    def get(self,request):
        Periods = ClassroomPeriod.objects.all()
        serializer = ClassroomPeriodSerializer(Periods,many=True)
        return Response(serializer.data)
    
class CoursesListView(APIView):
    def get(self,request):
        Periods = Courses.objects.all()
        serializer = CoursesSerializer(Periods,many=True)
        return Response(serializer.data)
    
class TeacherListView(APIView):
    def get(self,request):
        Teachers = Teacher.objects.all()
        serializer = TeacherSerializer(Teachers, many=True)
        return Response(serializer.data)
    
class StudentDetailView(APIView):
    def get(self,request,id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    def put(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status. HTTP_400_BAD_REQUEST)

    def delete(self,request, id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    



class Classroom_PeriodView(APIView):
    def get(self, request):
        class_periods = ClassroomPeriod.objects.all()
        serializer = ClassroomPeriodSerializer(class_periods, many=True)
        return Response(serializer.data)
class ClassListView(APIView):
    def get(self, request):
        classPeriod = ClassroomPeriod.objects.all()
        serializer = ClassroomPeriodListView(classPeriod,many=True)
        return Response(serializer.data)
class ClassDetailView(APIView):
    def get(self, request, id):
        classPeriod = ClassroomPeriod.objects.get(id = id)
        serializer = ClassroomPeriodSerializer(classPeriod)
        return Response(serializer.data)
    def post(self,request):
        serializer = ClassroomPeriodSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,id):
        classPeriod= ClassroomPeriod.objects.get(id=id)
        serializer =StudentSerializer (classPeriod)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request,id):
        classPeriod =ClassroomPeriod.objects.get(id=id)
        classPeriod.delete()
        return Response (status=status.HTTP_202_ACCEPTED)
class TeacherView(APIView):
    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        return Response(serializer.data)
class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
class TeacherDetailView(APIView):
    def get(self, request, id):
        teacher = Teacher.objects.get(id = id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
    def post(self,request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,id):
        teacher= Teacher.objects.get(id=id)
        serializer =TeacherSerializer(teacher)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request,id):
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return Response (status=status.HTTP_202_ACCEPTED)
class CoursesView(APIView):
    def get(self, request):
        course = Courses.objects.all()
        serializer = CoursesSerializer(course, many=True)
        return Response(serializer.data)
class CourseListView(APIView):
    def get(self, request):
        course = Courses.objects.all()
        serializer = CoursesSerializer(course, many=True)
        return Response(serializer.data)
class CourseDetailView(APIView):
    def get(self, request, id):
        course = Courses.objects.get(id = id)
        serializer = CoursesSerializer(course)
        return Response(serializer.data)
    def post(self,request):
        serializer = CoursesSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:ClassroomPeriod
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,id):
        course= Courses.objects.get(id=id)
        serializer =CoursesSerializer(course)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request,id):
        course = Courses.objects.get(id=id)
        course.delete()
        return Response (status=status.HTTP_202_ACCEPTED)
class ClassProjectView(APIView):
    def get(self, request):
        classroom = Class.objects.all()
        serializer = ClassesSerializer(Class, many = True)
        return Response(serializer)
class ClassProjectListView(APIView):
    def get(self, request):
        classroom = Class.objects.all()
        serializer = Class(classroom, many=True)
        return Response(serializer.data)
class ClassProjectDetailView(APIView):
    def get(self, request, id):
        classroom= Class.objects.get(id = id)
        serializer = Class(classroom)
        return Response(serializer.data)
    def post(self,request):
        serializer = ClassesSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,id):
        classroom= Class.objects.get(id=id)
        serializer =ClassesSerializer(classroom)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request,id):
        classroom = Class.objects.get(id=id)
        classroom.delete()
        return Response (status=status.HTTP_202_ACCEPTED)


   


