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

