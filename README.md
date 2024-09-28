# Ex02 Django ORM Web Application
## Date: 28.9.2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).


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
```
Admin.py

from django.contrib import admin
from .models import Bankloan, BankloanAdmin  


admin.site.register(Bankloan, BankloanAdmin)

Models.py

from django.db import models
from django.contrib import admin

class Bankloan(models.Model):
    loanid = models.IntegerField(primary_key=True)
    creditscore = models.IntegerField()
    age = models.IntegerField()  
    account_no = models.IntegerField()
    loan_purpose = models.IntegerField()

class BankloanAdmin(admin.ModelAdmin):
    list_display = ('loanid', 'creditscore', 'age', 'account_no', 'loan_purpose')  
```



## OUTPUT
![alt text](<Screenshot 2024-09-28 165003.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
