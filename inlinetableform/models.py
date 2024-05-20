# models.py
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    age = models.IntegerField()
# inline table
class BookDetail(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    publish_date = models.DateField()
    price = models.IntegerField()
    
class Consignment(models.Model):
    cnno = models.CharField(max_length=100)
    cndate = models.DateField()
    remark = models.CharField(max_length=100)
class InvoiceDetail(models.Model):
    consignment = models.ForeignKey(Consignment, on_delete=models.CASCADE)
    inno = models.CharField(max_length=100)
    indate = models.DateField()
    invalue = models.IntegerField()
class PartDetail(models.Model):
    invoice_detail = models.ForeignKey(InvoiceDetail, on_delete=models.CASCADE)
    part_name = models.CharField(max_length=100)