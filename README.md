# Ex02 Django ORM Web Application
## Date: 28/10/2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![alt text](<Screenshot 2024-10-27 143908.png>)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
from django.db import models
from django.contrib import admin
clasfroms Costumer(models.Model):
  cid=models.CharField(max_length=20,primary_key="eid")
  accountnumber=models.IntegerField()
  name=models.CharField(max_length=20)
  age=models.IntegerField()
  address=models.CharField(max_length=50)
  phonenumber=models.IntegerField()


class CostumerAdmin(admin.ModelAdmin):
  list_display=('cid','accountnumber','name','age','address','phonenumber')

from django.contrib import admin
from.models import Costumer,CostumerAdmin
admin.site.register(Costumer,CostumerAdmin)	

## OUTPUT

![alt text](<Screenshot 2024-10-27 133253.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
