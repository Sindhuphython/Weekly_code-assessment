from rest_framework import serializers
from patient.models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields=('p_code','name','address','disease','username','password')