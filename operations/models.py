from django.db import models
from django.contrib.auth.models import User

class Consignment(models.Model):
    consignment_no = models.AutoField(primary_key=True)
    consignment_date = models.DateField()
    source = models.CharField(max_length=100, null=True)
    destination = models.CharField(max_length=100, null=True)
    mode = models.CharField(max_length=100, null=True)
    billing_at = models.CharField(max_length=100, null=True)
    consignor = models.CharField(max_length=100, null=True)
    consignee = models.CharField(max_length=100, null=True)
    billing_party = models.CharField(max_length=100, null=True)
    delivery_at = models.CharField(max_length=100, null=True)
    load_type = models.CharField(max_length=100, null=True)

    # ForeignKey to the User model
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Consignment {self.consignment_no}"

class Invoice(models.Model):
    consignment_no = models.ForeignKey(Consignment, on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=100)
    invoice_date = models.DateField()
    invoice_description = models.CharField(max_length=100)
    part_code = models.CharField(max_length=100)
    invoice_value = models.CharField(max_length=100)
