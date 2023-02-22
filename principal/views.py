from django.shortcuts import render
from school_admin.models import Principal,Teachers,Classdivision,Classroom
from .models import Exams
from Teacher.models import Students

# Create your views here.

def view_teacher_page(request):
    teacher= Teachers.objects.all()
    classs=Classdivision.objects.all()

    return render(request,'principal/view_teacher.html',{'data':teacher,'class':classs}) 

def view_student_page(request):
    student =  Students.objects.all()
    return render(request,'school_admin/view_student.html',{'data1':student}) 

def add_exams(request):
    grade=Classroom.objects.all()
    if request.method == 'POST':
        exam=request.POST['exam']
        grades=request.POST['grade']
        grades=int(grades)
        classrm=Classroom.objects.get(id=grades)
        exams=Exams.objects.create(
            Examname=exam,
            grade_id=classrm.id

        )


    return render(request,'principal/add_exams.html',{'dat':grade})    

def principal_home_page(request):
    princi=Principal.objects.get(id=request.session['principalid'])
    return render(request,'principal/principal_home.html',{'data':princi})



def class_teacher_page(request):
    tchr=Teachers.objects.all()
    cls=Classdivision.objects.all()
    if request.method=='POST':
        print('hkhi')
        classname=request.POST['class']
        teachr=request.POST['teacher']
        classs=Classdivision.objects.get(id=int(classname))
        teach=Teachers.objects.get(id=int(teachr))
        classs.teacher_id=teach.id
        classs.save()
    return render(request,'principal/assign_class_teacher.html',{'class':cls,'teacher':tchr})