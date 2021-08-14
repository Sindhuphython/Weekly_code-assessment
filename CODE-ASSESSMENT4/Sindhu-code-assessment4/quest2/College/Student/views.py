from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

# Create your views here.
@csrf_exempt
def myStudentPage(request):
    if(request.method=="POST"):
        getName=request.POST.get("name")
        getAdmissionNumber=request.POST.get("adminno")
        getRollNumber=request.POST.get("rollno")
        getCollege=request.POST.get("college")
        getParentName=request.POST.get("parentname")
        dict={"name":getName,"adminno":getAdmissionNumber,"rollno":getRollNumber,"college":getCollege,"parentname":getParentName}
        result=json.dumps(dict)
        return HttpResponse(result)
    else:
        return HttpResponse("No GET method Allowed")

