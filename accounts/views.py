from django.shortcuts import render
# from .models import City
# from master.models import partyMaster
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def navbar(request):
    # objs = partyMaster.objects.values_list('partyname')
    # print(objs)
    context = {'page':'Accounts'}
    return render(request, 'accounts/navbar.html', context)

@login_required(login_url='/')
def bill_journal(request):
    context = {'page':'Bill Journal'}
    return render(request, 'billJournal/bill_journal.html', context)
    
@login_required(login_url='/')
def get_names(request):
    search = request.GET.get('search')
    payload = []
    if search:
        objs = City.objects.filter(name__startswith = search)
        for obj in objs:
            payload.append({
                'name': obj.name
            })
    return JsonResponse({
        'status' : True,
        'payload' : payload,
    })