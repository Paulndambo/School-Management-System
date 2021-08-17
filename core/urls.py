from django.urls import path
from . views import *
from . import views

urlpatterns = [
	path("", views.home, name="home"),
	path("teachers/", TeachersList.as_view(), name="teachers"),
	path("new-teacher/", NewTeacher.as_view(), name="new-teacher"),
	path("students/", StudentsList.as_view(), name="students"),
	path("new-student/", NewStudent.as_view(), name="new-student"),
	path("subjects/", SubjectsList.as_view(), name="subjects"),
	path("new-subject/", NewSubject.as_view(), name="new-subject"),
	path("marks/", MarkList.as_view(), name="marks"),
	path("new-marks/", NewMarks.as_view(), name="new-marks"),
]