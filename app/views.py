from django.shortcuts import redirect, render
from .models import Student
from .forms import StudentForm


# Create your views here.
def home(request):
   
   return render(request, "app/home.html")

def student_list_view(request):
    students = Student.objects.all() 
            
    context = {
        "students":students,
      
    }
    return render(request, "app/student_list.html", context)

def student_add_view(request):
    
    form = StudentForm()
    
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("list")
        
    context = {
        "form":form,
    }
    return render(request, "app/student_add.html", context)

def student_detail_view(request, id):
    
    student = Student.objects.get(id = id)
    
    context = {
        "student":student,
        
    }
    
    return render(request, "app/student_detail.html",context)

def student_update_view(request, id):
    student = Student.objects.get(id = id)
    form = StudentForm(instance = student)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance = student)
        if form.is_valid():
            form.save()
            return redirect("list")    
    
    context = {
        "student":student,
        "form":form
        
    } 
    return render(request, "app/student_update.html", context)


def student_delete_view(request, id):
    
    dlt = Student.objects.get(id = id)
    if request.method == "POST": 
        dlt.delete()
        return redirect("list")
    
    context = {
        "student":dlt       
        
    }
    
    return render(request, "app/delete.html", context)