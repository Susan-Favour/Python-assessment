from rest_framework import serializers
from student.models import Student
from classroom_period.models import ClassroomPeriod

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class ClassroomPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClassroomPeriod
        fields = "__all__"

