from django.db import models
from teacher.models import Teacher
from student.models import Student
# Create your models here.
class Courses(models.Model):
    course_name = models.CharField(max_length = 20)
    course_id = models.SmallIntegerField()
    department = models.CharField(max_length = 20)
    course_description = models.TextField()
    class_starting_time = models.TimeField(00, 00, 00)
    course_trainer_name = models.CharField(max_length=100)
    number_of_students = models.PositiveSmallIntegerField()
    grade_level = models.PositiveSmallIntegerField()
    school_term = models.IntegerField()
    assement_requirements = models.TextField()
    course_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')
    course_students = models.ManyToManyField(Student, related_name='courses')
    def __str__(self):
        return f"{self.course_name} {self.course_trainer_name}"