from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.
GENDER_CHOICES = (
	("Male", "Male"),
	("Female", "Female"),
)

CLASSES_CHOICES = (
	("1", "1"),
	("2", "2"),
	("3", "3"),
	("4", "4"),
	("5", "5"),
	("6", "6"),
	("7", "7"),
	("8", "8"),
)

class Teacher(models.Model):
	user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
	phone_number = models.CharField(max_length=20)
	gender = models.CharField(max_length=200, choices=GENDER_CHOICES)
	postal_code = models.CharField(max_length=200)
	town = models.CharField(max_length=200)
	country =models.CharField(max_length=200)

	def __str__(self):
		return self.user.username

	def get_absolute_url(self):
		return reverse("teachers")

class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
	admission_number = models.CharField(max_length=200, unique=True)
	phone_number =models.CharField(max_length=20)
	gender = models.CharField(max_length=200, choices=GENDER_CHOICES)
	admission_date = models.DateField(default=timezone.now)
	current_class = models.CharField(max_length=200, choices=CLASSES_CHOICES)
	postal_code = models.CharField(max_length=200)
	town = models.CharField(max_length=200)
	country =models.CharField(max_length=200)

	def __str__(self):
		return self.user.username

	def get_absolute_url(self):
		return reverse("students")

class Subject(models.Model):
	code = models.CharField(max_length=10, unique=True, primary_key=True)
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("subjects")

class Mark(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	marks = models.FloatField(default=0)

	def __str__(self):
		return (self.student)

	def get_absolute_url(self):
		return reverse("marks")