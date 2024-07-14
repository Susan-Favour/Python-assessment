from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student
from .serializers import StudentSerializer
from classroom_period.models import ClassroomPeriod
from .serializers import ClassroomPeriodSerializer


class StudentListViews(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many = True)
        return Response(serializer.data)
    
class ClassRoomListView(APIView):
    def get(self,request):
        periods = ClassroomPeriod.objects.all()
        serializer = ClassroomPeriodSerializer(periods, many=True)
        return Response(serializer.data)
