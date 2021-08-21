from django.shortcuts import render
from patient.models import Patient
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from patient.serializers import PatientSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.
def patient_view(request):
    return render(request,'add.html') 

@csrf_exempt
def patient_create(request):
    if(request.method=="POST"):
        mydata=JSONParser().parse(request)
        patient_serialize=PatientSerializer(data=mydata)
        if(patient_serialize.is_valid()):
            patient_serialize.save()
            return JsonResponse(patient_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("Get Method Not Allowed",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def patient_list(request):
    if(request.method=="GET"):
        patients=Patient.objects.all()
        patient_serializer=PatientSerializer(patients,many=True)
        return JsonResponse(patient_serializer.data,safe=False)

@csrf_exempt
def patient_details(request,id):
    try:
        patients=Patient.objects.get(id=id)
        if(request.method=="GET"):
            patient_serializer=PatientSerializer(patients)
            return JsonResponse(patient_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            patients.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            patient_serialize=PatientSerializer(patients,data=mydata)
            if(patient_serialize.is_valid()):
                patient_serialize.save()
                return JsonResponse(patient_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(patient_serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    except Patient.DoesNotExist:
        return HttpResponse("Invalid Id",status=status.HTTP_404_NOT_FOUND)
@csrf_exempt
def patient(request,p_code):
        patients=Patient.objects.get(p_code=p_code)
        if(request.method=="GET"):
            patient_serializer=PatientSerializer(patients)
            return JsonResponse(patient_serializer.data,safe=False,status=status.HTTP_200_OK)

