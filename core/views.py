from django.shortcuts import render
from . models import *
from django.views.generic import ListView, UpdateView, CreateView, DetailView
# Create your views here.
def home(request):
	subjects = Subject.objects.all().count()
	teachers = Teacher.objects.all().count()
	students = Student.objects.all().count()

	context = {
		"students": students,
		"teachers": teachers,
		"subjects": subjects
	}
	return render(request, "index.html", context)

class TeachersList(ListView):
	model = Teacher
	template_name = "teachers.html"

class NewTeacher(CreateView):
	model = Teacher
	fields = "__all__"
	template_name = "new-teacher.html"

class StudentsList(ListView):
	model = Student
	template_name = "students.html"

class NewStudent(CreateView):
	model = Student
	fields = "__all__"
	template_name = "new-student.html"

class SubjectsList(ListView):
	model = Subject
	template_name = "subjects.html"

class NewSubject(CreateView):
	model = Subject
	fields = "__all__"
	template_name = "new-subject.html"

class MarkList(ListView):
	model = Mark
	template_name = "marks.html"

class NewMarks(CreateView):
	model = Mark
	fields = "__all__"
	template_name = "new-mark.html"