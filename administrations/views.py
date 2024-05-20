from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.
@login_required(login_url='/')
def navbar(request):
    context = {'page':'Administrations'}
    return render(request, 'administrations/navbar.html', context)

# @login_required(login_url='/')
def users(request):
    userPage = {'page':'User Master'}
    if request.method == 'POST':
        data = request.POST

        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        password = data.get('password')
        
        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request, 'Username already created')
            return redirect('/administrations/users/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )
        
        user.set_password(password)
        user.save()
        
        messages.info(request, 'User created sussfully')
        return redirect('/administrations/users/')

    queryset = User.objects.all()
    context = {
        **userPage,
        'users':queryset,
    }

    return render(request, 'securityManager/users.html', context)

# @login_required(login_url='/')
def usersList(request):
    items_per_page = 5
    queryset = User.objects.order_by('id')
    print(queryset)
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
        'page' : 'User List',
    }
    return render(request, 'securityManager/usersList.html', context)

def get_party_list(request):
    search = request.GET.get('search')
    payload = []
    if search:
        # objs = User.objects.values_list('first_name')
        objs = User.objects.filter(first_name__startswith = search)
        for obj in objs:
            payload.append({
                'first_name':obj.first_name
            })
        return JsonResponse({
            'status' : True,
            'payload' : payload,
        })