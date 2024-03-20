from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Consignment, Invoice
import json

def operation(request):
    return render(request, 'operation_nav/operation_nav.html')

def consignment_form(request):
    return render(request, 'index.html')

@csrf_exempt
def create_consignment_with_invoices(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        # Create a consignment
        consignment = Consignment.objects.create(
            consignment_no=data['consignmentNo'],
            consignment_date=data['consignmentDate'],
            from_field=data['from'],
            to=data['to']
        )

        # Create multiple invoices and associate them with the consignment
        for invoice_data in data['invoices']:
            Invoice.objects.create(
                consignment=consignment,
                invoice_no=invoice_data['invoiceNo'],
                invoice_date=invoice_data['invoiceDate']
            )

        return JsonResponse({'success': True, 'consignment_id': consignment.id})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})