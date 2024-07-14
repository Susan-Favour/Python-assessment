from django.urls import path
from .views import StudentListViews
from .views import ClassRoomListView

urlpatterns = [
    path('students/', StudentListViews.as_view(),
         name = "student_list_view" ),
    path(
        "periods/", ClassRoomListView.as_view(), name = "classroomPeriods_list_view"
    )
]
