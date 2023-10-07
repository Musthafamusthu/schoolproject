
from django.db import models
from django.db.models import CASCADE
# Create your models here.
class login(models.Model):
    uname=models.CharField(max_length=100)
    password=models.IntegerField()
    def __str__(self):
        return self.uname
class Department(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name
class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
class Detailsmodel(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(max_length=10)
    age = models.IntegerField()
    GENDER_CHOICES = (
            ('M', 'Male'),
            ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    # gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    phone = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=500, null=True, unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    purposes = (
        ('enqry', 'Enquiry'),
        ('order', 'Placeorder'),
        ('return', 'Placereturn'),
    )
    purpose = models.CharField(max_length=6, choices=purposes, default='enqry')
    matprov = (
        ('debit', 'debitcard'),
        ('crdt', 'creditcard'),
        ('cheque', 'chequebook'),
    )
    materialprovides = models.CharField(max_length=100, choices=matprov)

    def __str__(self):
        return self.name