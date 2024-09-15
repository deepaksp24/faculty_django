from django.http import HttpResponse
from django.shortcuts import render
from .models import Faculty

# Create your views here.


def startPage(request):
    return render(request, 'index.html')


def addFacultyForm(request):
    return render(request, 'facultyForm.html')


def addFaculty(request):
    name = request.POST['fName']
    dept = request.POST['fDept']
    sal = request.POST['fSal']
    print(name)

    facultyInstance = Faculty(fName=name, fDept=dept, fSal=sal)
    facultyInstance.save()
    return HttpResponse("saved successfully ")


def featchFaculty(request):
    faculties = Faculty.objects.all()
    return render(request, 'facultyList.html', {'faculties': faculties})


def deleteFacultyForm(request):
    return render(request, 'deleteFacultyForm.html')


def deleteFaculty(request):
    facultyId = request.POST['id']
    faculty = Faculty.objects.filter(id=facultyId)
    if faculty:
        Faculty.objects.filter(id=facultyId).delete()
        return HttpResponse("deleted sucessfully")
    else:
        return HttpResponse("No such ID found")


def updateFacultyForm(request):
    return render(request, 'updateFacultyForm.html')


def updateFaculty(request):
    facultyId = request.POST['fId']
    try:
        faculty = Faculty.objects.get(id=facultyId)
    except Faculty.DoesNotExist:
        # print(faculty)
        return HttpResponse("No such ID found please enter the exiting ID")
    name = request.POST['fName']
    dept = request.POST['fDept']
    sal = request.POST['fSal']
    if name:
        faculty.fName = name
    if dept:
        faculty.fDept = dept
    if sal:
        faculty.fSal = sal
    faculty.save()
    return HttpResponse("update successfully")
