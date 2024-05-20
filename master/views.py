from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/')
def navbar(request):
    context = {'page':'Masters'}
    return render(request, 'navbar.html', context)

@login_required(login_url='/')
def state(request):
    if request.method == 'POST':
        data = request.POST
        stateMaster.objects.create(
            name = data.get('name'),
            code = data.get('code'),
            gstcode = data.get('gstcode'),
            gstin = data.get('gstin'),
            country = data.get('country'),
            frompin = data.get('frompin'),
            topin = data.get('topin'),
        )
        return redirect('/master/state/')
    
    queryset = stateMaster.objects.all()
    context = {
        'page':'State',
        'state': queryset,
        
    }
    return render(request, 'state/state.html', context)

@login_required(login_url='/')
def statelist(request):
    item_per_page = 5
    queryset = stateMaster.objects.order_by('id')
    countstate = stateMaster.objects.all().count()
    
    paginator = Paginator(queryset, item_per_page)
    page = request.GET.get('page')
    try:
        serviceData = paginator.page(page)
    except PageNotAnInteger:
        serviceData = paginator.page(1)
    except EmptyPage:
        serviceData = paginator.page(paginator.num_pages)
    context = {
        'serviceData': serviceData,
        'count' : countstate,
        'page':'State List'
    }
    return render(request, 'state/statelist.html', context)

@login_required(login_url='/')
def updatestate(request, id):
    updt = stateMaster.objects.get(id = id)
    data = request.POST
    if request.method == 'POST':
        updt.name = data.get('name')
        updt.code = data.get('code')
        updt.gstcode = data.get('gstcode')
        updt.gstin = data.get('gstin')
        updt.country = data.get('country')
        updt.frompin = data.get('frompin')
        updt.topin = data.get('topin')
        
        updt.save()
        return redirect('/master/statelist/')
        
    context = {
        'updatestate':updt,
        'page':'Update State'
    }
    return render(request, 'state/stateupdate.html', context)

@login_required(login_url='/')
def deletestate(request, id):
    dlt = stateMaster.objects.get(id = id)
    dlt.delete()
    return redirect('/master/statelist/')

@login_required(login_url='/')
def party(request):
    if request.method == 'POST':
        data = request.POST
        partyMaster.objects.create(
            partytype = data.get("partytype"),
            code = data.get("code"),
            group = data.get("group"),
            expensetype = data.get("expensetype"),
            partyname = data.get("partyname"),
            controllingbranch = data.get("controllingbranch"),
            parentaccount = data.get("parentaccount"),
            address = data.get("address"),
            city = data.get("city"),
            state = data.get("state"),
            pin = data.get("pin"),
            country = data.get("country"),
            contactperson = data.get("contactperson"),
            mobilenumber = data.get("mobilenumber"),
            email = data.get("email"),
            
            nameco = data.get('nameco'),
            mobileco = data.get('mobileco'),
            departmentco = data.get('departmentco'),
            branchco = data.get('branchco'),
            
            registrationtype = data.get("registrationtype"),
            servicetype = data.get("servicetype"),
            gstin = data.get("gstin"),
            
            gstinverify = data.get('gstinverify'),
            
            pan = data.get("pan"),
            tdsdeducation = data.get("tdsdeducation"),
            
            turnoverfivecr = data.get('turnoverfivecr'),
            declarationsubmit = data.get('declarationsubmit'),
            einvoiceapli = data.get('einvoiceapli'),
        )
        return redirect('/master/party/')
    
    queryset = partyMaster.objects.all()
    context = {
        'page':'Party Master',
        'party':queryset,
    }
    return render(request, 'party/party.html', context)

@login_required(login_url='/')
def partylist(request):    
    items_per_page = 5  # You can adjust this based on your preference

    # Order the queryset based on a specific field, for example, 'id'
    queryset = partyMaster.objects.order_by('id')
    countparty = partyMaster.objects.all().count()
    paginator = Paginator(queryset, items_per_page)
    page = request.GET.get('page')
    try:
        serviceData = paginator.page(page)
    except PageNotAnInteger:
        serviceData = paginator.page(1)
    except EmptyPage:
        serviceData = paginator.page(paginator.num_pages)
        
    context = {
        'serviceData': serviceData,
        'count' : countparty,
        'page' : 'Party Master List',
    }
    return render(request, 'party/partylist.html', context)
    
@login_required(login_url='/')
def updateparty(request, id):
    updt = partyMaster.objects.get(id = id)
    data = request.POST
    if request.method == 'POST':
        updt.partytype = data.get("partytype")
        updt.code = data.get("code")
        updt.group = data.get("group")
        updt.expensetype = data.get("expensetype")
        updt.partyname = data.get("partyname")
        updt.controllingbranch = data.get("controllingbranch")
        updt.parentaccount = data.get("parentaccount")
        updt.address = data.get("address")
        updt.city = data.get("city")
        updt.state = data.get("state")
        updt.pin = data.get("pin")
        updt.country = data.get("country")
        updt.contactperson = data.get("contactperson")
        updt.mobilenumber = data.get("mobilenumber")
        updt.email = data.get("email")
        
        updt.nameco = data.get('nameco')
        updt.mobileco = data.get('mobileco')
        updt.departmentco = data.get('departmentco')
        updt.branchco = data.get('branchco')
        
        updt.registrationtype = data.get("registrationtype")
        updt.servicetype = data.get("servicetype")
        updt.gstin = data.get("gstin")
        
        updt.gstinverify = data.get('gstinverify')
        
        updt.pan = data.get("pan")
        updt.tdsdeducation = data.get("tdsdeducation")
        
        updt.turnoverfivecr = data.get('turnoverfivecr')
        updt.declarationsubmit = data.get('declarationsubmit')
        updt.einvoiceapli = data.get('einvoiceapli')
        
        updt.save()
        return redirect('/master/partylist/')

    context = {
        'updateparty':updt,
        'page':'Update Party',
    }
    return render(request, 'party/partyupdate.html', context)

@login_required(login_url='/')
def deleteparty(request, id):
    # dlt = partyMaster.objects.get(id = id)
    # dlt.delete()
    return redirect('/master/party/')
