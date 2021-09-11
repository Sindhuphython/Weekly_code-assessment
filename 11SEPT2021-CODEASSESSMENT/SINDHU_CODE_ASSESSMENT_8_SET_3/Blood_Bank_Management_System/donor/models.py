from django.db import models

# Create your models here.
class Donor(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    bloodgroup=models.CharField(max_length=50)
    mobileno=models.BigIntegerField()
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    id=models.AutoField(auto_created=True,primary_key=True,serialize=False)