from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django import http
from .forms import AttendeFormIn, AttendeFormOut
from .models import Attende

import datetime
now = datetime.datetime.now()
#temp = now.strftime('%Y-%m-%d %H:%M:%S.%f').replace(tzinfo=datetime.timezone.utc)

# Create your views here.
def index(request):

    #attende = Attende()
    form1 = AttendeFormIn()
    form2 = AttendeFormOut()

    if request.method == 'POST' and 'in' in request.POST:

        form1 = AttendeFormIn(request.POST)

        if form1.is_valid():
            form1.save()
            return http.HttpResponseRedirect('')
            #attende.intime = temp
            #attende.outtime = temp
            #attende.save()

    if request.method == 'POST' and 'out' in request.POST:
        form2 = AttendeFormOut(request.POST)
        #up_req = request.POST.copy()
        #up_req.update({'date_out_time': [datetime.now()]})
        #up_req.update({'date_out_time': [now.strftime('%Y-%m-%d %H:%M:%S.%f')]})
        #print(up_req)
        if form2.is_valid():
            #form2.date_out_time = (auto_now=True)
            userid = request.POST.get('uid')
            '''try:
                f = Attende.objects.get(uid = userid)
            except Attende.DoesNotExist:
                return redirect('index')'''
            #if Attende.objects.get(uid=userid):
            #print(now.strftime('%Y-%m-%d %H:%M:%S.%f'))
            try:
                l = Attende.objects.filter(uid=userid).last()
                lpk = l.pk
                #print(lpk)
                #print(type(lpk))
                Attende.objects.filter(id=lpk).update(date_out_time=now.strftime('%Y-%m-%d %H:%M:%S.%f'))
            except InDoesNotExist:
                print("In required")

            #form2.save()
            return http.HttpResponseRedirect('')
            #form2.save()
            #Attende.objects.filter(fieldname="uid")
    context = {'form1': form1, 'form2': form2}
    return render(request, 'logging/index.html', context)

def details():
    data1 = Attende.objects.get(uid=userid)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)