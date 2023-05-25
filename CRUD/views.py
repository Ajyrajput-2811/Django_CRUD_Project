from django.shortcuts import render,redirect
from .form import *
from .models import *

def home(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            rf = Student(name = nm,email=em,password = pw)
            rf.save()
            fm  = StudentRegistration()    
        
    else:
        fm  = StudentRegistration()  
    student = Student.objects.all()  
    return render(request,'index.html',{'form':fm,'stu':student})

def delete_data(request,id):
    if request.method == "POST":
        pi = Student.objects.get(pk=id) 
        pi.delete()
        return redirect(home) 


def updated_data(request,id):
    pi  = Student.objects.get(pk=id) 
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            rf = Student(id= id,name = nm , email=em,password = pw)
            rf.save()
            return redirect(home)
    else:
        pi  = Student.objects.get(pk=id) 
        fm = StudentRegistration(instance=pi)
    return render(request,'update.html',{'form':fm})    


    







