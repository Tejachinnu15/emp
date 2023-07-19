from django.db import models

# Create your models here.
class Dept(models.Model):
    DNO=models.IntegerField(max_length=100,primary_key=True)
    DNAME=models.CharField(max_length=100)
    DLOC=models.CharField(max_length=100)
class Emp(models.Model):
    ENO=models.IntegerField(max_length=100)
    ENAME=models.CharField(max_length=100)
    MGR=models.CharField(max_length=100)
    HIRE_DATE=models.DateField()
    DNO=models.ForeignKey(Dept,on_delete=models.CASCADE)
