from django.shortcuts import render,HttpResponseRedirect
from .models import Student, MY_CHOICES
from .forms import StudentRegistration
from django.db.models import Q

# Retrieves a list of all students and renders them to the 'show.html' template
def show (request):
    student=Student.objects.all()
    return render (request, "crudapp/show.html",{'student':student})


 # Form for creating or updating student records
def adddata(request):
    if request.method == "POST":
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/")
    else:
        fm=StudentRegistration()
    return render (request,"crudapp/adddata.html",{'form':fm})


 # Form for updating student records
def updatedata(request ,id):
    if request.method=="POST":
        student=Student.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=student)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect("/")
    else:
        student=Student.objects.get(pk=id)
        fm=StudentRegistration(instance=student)
    return render (request, "crudapp/update.html",{'form':fm})

 # Form for deleting student records
def deletedata(request ,id):
    if request.method=="POST":
        student=Student.objects.get(pk=id)
        student.delete()
        return HttpResponseRedirect("/")

# Retrieves a list of all students accordinng to keyword
def searchstudent(request):
    if request.method == 'POST':
        n1 = request.POST.get('output')
        print(n1)
        student = Student.objects.all()
        std = None  # Initialize the variable
        if n1:
            std = student.filter(
                Q(fname__icontains=n1) |
                Q(lname__icontains=n1) |
                Q(email__icontains=n1) |
                Q(phone__icontains=n1) |
                Q(branch__icontains=n1)
            )
            print( std.count())
        return render(request, "crudapp/show.html", {'student': std})
    else:
        return HttpResponse('An Exception Occurred')
