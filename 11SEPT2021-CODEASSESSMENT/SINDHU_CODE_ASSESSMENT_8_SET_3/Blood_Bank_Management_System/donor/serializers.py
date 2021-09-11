from rest_framework import serializers
from donor.models import Donor

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Donor
        fields=('id','name','address','bloodgroup','mobileno','username','password')