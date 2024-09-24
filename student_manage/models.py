from django.db import models

/*This are courses that students are enrolled*/
MY_CHOICES = [
        ("CE", 'CE'),
        ("EXTC", 'EXTC'),
        ("ME", 'ME'),
        ("AI", 'AI'),
        ("IT", 'IT'),
    ]

/*creating a model for student inf0*/
class Student(models.Model):
    fname=models.CharField(max_length=25)
    lname=models.CharField(max_length=25)
    email=models.EmailField(max_length=25)
    phone=models.PositiveIntegerField()
    branch=models.CharField(max_length=50,choices=MY_CHOICES)
        
/* defining the string function for our model*/
    def __str__(self):
        return self.fname
