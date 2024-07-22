from django.db import models
from classes.models import Class
from courses.models import Courses
# Create your models here.

class ClassroomPeriod(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='classroom_periods')
    day_of_the_week = models.DateField()
    class_room= models.ForeignKey(Class, on_delete=models.CASCADE, related_name='classroom_periods')  # New field

    def __str__(self):
        return f"{self.start_time} {self.classroom}"

