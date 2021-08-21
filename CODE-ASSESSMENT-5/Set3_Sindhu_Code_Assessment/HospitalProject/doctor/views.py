from django.shortcuts import render
from doctor.models import Doctor
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from doctor.serializers import DoctorSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.
def doctor_view(request):
    return render(request,'register.html')
def doctor_view(request):
    return render(request,'login.html')

def doctor_create(request):
    if(request.method=="POST"):
        mydata=JSONParser().parse(request)
        doctor_serialize=DoctorSerializer(data=mydata)
        if(doctor_serialize.is_valid()):
            doctor_serialize.save()
            return JsonResponse(doctor_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("Get Method Not Allowed",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def doctor_list(request):
    if(request.method=="GET"):
        doctors=Doctor.objects.all()
        doctor_serializer=DoctorSerializer(doctors,many=True)
        return JsonResponse(doctor_serializer.data,safe=False)

@csrf_exempt
def doctor_details(request,id):
    try:
        doctors=Doctor.objects.get(id=id)
        if(request.method=="GET"):
            doctor_serializer=DoctorSerializer(doctors)
            return JsonResponse(doctor_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            doctors.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            doctor_serialize=DoctorSerializer(doctors,data=mydata)
            if(doctor_serialize.is_valid()):
                doctor_serialize.save()
                return JsonResponse(doctor_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(doctor_serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    except Doctor.DoesNotExist:
        return HttpResponse("Invalid Id",status=status.HTTP_404_NOT_FOUND)
@csrf_exempt
def doctor(request,d_code):
        doctors=Doctor.objects.get(d_code=d_code)
        if(request.method=="GET"):
            doctor_serializer=DoctorSerializer(doctors)
            return JsonResponse(doctor_serializer.data,safe=False,status=status.HTTP_200_OK)
