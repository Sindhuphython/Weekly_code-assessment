from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt
def MyFacultyPage(request):
    if(request.method=="POST"):
        getName=request.POST.get("name")
        getAddress=request.POST.get("facaddress")
        getDepartment=request.POST.get("dept")
        getCollege=request.POST.get("college")
        dict={"name":getName,"facaddress":getAddress,"dept":getDepartment,"college":getCollege}
        result=json.dumps(dict)
        return HttpResponse(result)
    else:
        return HttpResponse("No GET method Allowed")
