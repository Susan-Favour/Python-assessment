from django.urls import path
from .views import StudentListViews
from .views import ClassroomPeriodListView
from .views import ClassRoomListView
from .views import CoursesListView
from .views import TeacherListView
urlpatterns = [
    path(
        "students/",StudentListViews.as_view(),name="student_list_view"
    ),
    path(
        "classes/", ClassroomPeriodListView.as_view(), name="class_list_view"
    ),
    path(
        "periods/", ClassRoomListView.as_view(), name="classroomPeriod_list_view"
    ),
    path(
        "courses/", CoursesListView.as_view(), name="course_list_view"
    ),
    path(
        "teachers/", TeacherListView.as_view(), name="teachers_list_view"
    )
]