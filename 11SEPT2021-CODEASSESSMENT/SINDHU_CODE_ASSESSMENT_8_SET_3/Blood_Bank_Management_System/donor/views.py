from django.shortcuts import redirect,render
from donor.models import Donor
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from donor.serializers import DonorSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests
#add donor
def signin_view(request):
    return render(request,'signin.html')
def welcome_view(request):
    return render(request,'welcome.html')
@csrf_exempt
def signin_view_check(request):
    try:
        username=request.POST.get("username")
        password=request.POST.get("password")
        getdonor=Donor.objects.filter(username=username,password=password)
        donor_serializer=DonorSerializer(getdonor,many=True)
        print(donor_serializer.data)
        if(donor_serializer.data):
            for i in donor_serializer.data:
                a=i["name"]
                b=i["address"]
                c=i["bloodgroup"]
                d=i["mobileno"]
                e=i["id"]
                print(a)
            request.session['uname']=a
            request.session['uaddress']=b
            request.session['ubloodgroup']=c
            request.session['umobileno']=d
            request.session['uid']=e
            return render(request,"welcome.html")
        else:
            return HttpResponse("Invalid Credentials")
    except Donor.DoesNotExist:
        return HttpResponse("Invalid name",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Went Wrong")
        
def viewall_donor_view(request):
    fetchdata=requests.get("http://127.0.0.1:8000/donor/viewall/").json()
    return render(request,'viewall.html',{"data":fetchdata})
@csrf_exempt
def donor_create(request):
    if(request.method=="POST"):
        # mydata=JSONParser().parse(request)
        donor_serialize=DonorSerializer(data=request.POST)
        if(donor_serialize.is_valid()):
            donor_serialize.save()
            return redirect(viewall_donor_view)
            # return JsonResponse(donor_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("Get Method Not Allowed",status=status.HTTP_404_NOT_FOUND)
@csrf_exempt
def donor_list(request):
    if(request.method=="GET"):
        donors=Donor.objects.all()
        donor_serializer=DonorSerializer(donors,many=True)
        return JsonResponse(donor_serializer.data,safe=False)
#update donor
@csrf_exempt
def donor_details(request,id):
    try:
        donors=Donor.objects.get(id=id)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            donor_serialize=DonorSerializer(donors,data=mydata)
            if(donor_serialize.is_valid()):
                donor_serialize.save()
                return JsonResponse(donor_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(donor_serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    except Donor.DoesNotExist:
        return HttpResponse("Invalid ID",status=status.HTTP_404_NOT_FOUND)
def add_donor_view(request):
    return render(request,'signup.html')

def update_donor_view(request):
    return render(request,'update.html')
@csrf_exempt
def updateapi(request):
    try:
        getname=request.POST.get("name")
        getaddress=Donor.objects.filter(name=getname)
        donor_serializer=DonorSerializer(getaddress,many=True)
        print(donor_serializer.data)
        # return JsonResponse(donor_serializer.data,safe=False,status=status.HTTP_200_OK)
        return render(request,"update.html",{"data":donor_serializer.data})
    except Donor.DoesNotExist:
        return HttpResponse("Invalid Name",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Went Wrong")
@csrf_exempt
def update_data_read(request):
    getnewid=request.POST.get("newid")
    getnewname=request.POST.get("newname")
    getnewaddress=request.POST.get("newaddress")
    getnewbloodgroup=request.POST.get("newbloodgroup")
    getnewmobileno=request.POST.get("newmobileno")
    getnewusername=request.POST.get("newusername")
    getnewpassword=request.POST.get("newpassword")
    mydata={'name':getnewname,'address':getnewaddress,'bloodgroup':getnewbloodgroup,
            'mobileno':getnewmobileno,'username':getnewusername,'password':getnewpassword}
    jsondata=json.dumps(mydata)
    print(jsondata)
    Apilink="http://127.0.0.1:8000/donor/viewdonor/"+getnewid
    requests.put(Apilink,data=jsondata)
    return redirect(viewall_donor_view)