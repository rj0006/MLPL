from django.contrib import admin
from .models import Consignment, Invoice
from django.contrib.auth import get_user_model

# For using add invoice in tabular form
class InvoiceInLineAdmin(admin.TabularInline):
    model = Invoice

class ConsignmentAdmin(admin.ModelAdmin):
    
    # inline foreinkey of invoice
    inlines = [InvoiceInLineAdmin]
    
    # This is for using if user is authenticate true then add current active user session save in the form of foreingkey inside consignment table
    model = Consignment
    fields = ('consignment_date', 'source', 'destination', 'mode', 'billing_at',
              'consignor', 'consignee', 'billing_party', 'delivery_at', 'load_type')  # Add other fields as needed
    def save_model(self, request, obj, form, change):
        # Set the user field to the currently logged-in user
        obj.user = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Consignment, ConsignmentAdmin)