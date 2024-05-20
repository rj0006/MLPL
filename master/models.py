from django.db import models
from django.contrib.auth.models import User
from administrations.models import User

# Create your models here.
class partyMaster(models.Model):
    # username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    partytype = models.CharField(max_length=50, null=True)
    code = models.CharField(max_length=50, null=True)
    group = models.CharField(max_length=50, null=True)
    expensetype = models.CharField(max_length=50, null=True)
    partyname = models.CharField(max_length=250, null=True, unique=True)
    controllingbranch = models.CharField(max_length=50, null=True)
    parentaccount = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    pin = models.IntegerField(null=True)
    country = models.CharField(max_length=50, null=True)
    contactperson = models.CharField(max_length=50, null=True)
    mobilenumber = models.IntegerField(null=True)
    email = models.CharField(max_length=50, null=True)
    registrationtype = models.CharField(max_length=50, null=True)
    servicetype = models.CharField(max_length=50, null=True)
    gstin = models.CharField(max_length=15, null=True)
    pan = models.CharField(max_length=10, null=True)
    tdsdeducation = models.IntegerField(null=True)
    
    nameco = models.CharField(max_length=50, null=True)
    mobileco = models.CharField(max_length=50, null=True)
    departmentco = models.CharField(max_length=50, null=True)
    branchco = models.CharField(max_length=50, null=True)
    gstinverify = models.CharField(max_length=50, null=True)
    turnoverfivecr = models.CharField(max_length=10, null=True)
    declarationsubmit = models.CharField(max_length=10, null=True)
    einvoiceapli = models.CharField(max_length=10, null=True)
    
class stateMaster(models.Model):
    # username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, unique=True)
    code = models.CharField(max_length=50, null=True)
    gstcode = models.CharField(max_length=50, null=True)
    gstin = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=250, null=True)
    frompin = models.CharField(max_length=50, null=True)
    topin = models.CharField(max_length=50, null=True)