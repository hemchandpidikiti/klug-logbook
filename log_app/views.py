from os import name
from django.core.validators import RegexValidator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django import http
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .forms import AttendeFormIn, AttendeFormOut, CreateUserForm, SaveForm
from .models import Attende
from .serializers import MasterSerializer
import pytz
import os
#import csv
# from datetime import datetime
import datetime
from .models import Master
#from log_app.ser import *
#tz_NY = pytz.timezone('Asia/Kolkata')
# datetime_NY = datetime.now(tz_NY)
IST = pytz.timezone('Asia/Kolkata')
#now1 = datetime.datetime.now(IST)
#print(now)


# temp = now.strftime('%Y-%m-%d %H:%M:%S.%f').replace(tzinfo=datetime.timezone.utc)

# Create your views here.
@login_required
def index(request):
    IST = pytz.timezone('Asia/Kolkata')
    #f = open("./static/csv/rfid.csv")

    #csvreader = csv.reader(f)
    #h = next(csvreader)

    form1 = AttendeFormIn()
    form2 = AttendeFormOut()
    now1 = datetime.datetime.now(IST)

    if request.method == 'POST' and 'in' in request.POST:

        form1 = AttendeFormIn(request.POST)

        if form1.is_valid():
            #print(form1)
            f1 = form1.save(commit=False)
            ron = request.user
            f1.room_name = ron.username
            userid = request.POST.get('uid')
            #print(userid)
            uid_value = Master.objects.filter(uid=userid).last()
            uid_name = uid_value.name
            #print(uid_name)
            f1.in_time = now1.strftime('%H:%M:%S.%f')
            f1.uname = uid_name
            #in_time = now1.strftime('%H:%M:%S.%f')
            f1.save()
            #purpose = request.POST.get('purpose')
            #print(purpose)
            #Attende.objects.create(room_name=ron.username, uid=userid, purpose=purpose, in_time=in_time)
            messages.success(request, f'{uid_name} You are IN')
            return http.HttpResponseRedirect('')
        else:
            messages.error(request, 'Enter correct User ID')
            # attende.intime = temp
            # attende.outtime = temp
            # attende.save()

    if request.method == 'POST' and 'out' in request.POST:
        form2 = AttendeFormOut(request.POST)
        # up_req = request.POST.copy()
        # up_req.update({'date_out_time': [datetime.now()]})
        # up_req.update({'date_out_time': [now.strftime('%Y-%m-%d %H:%M:%S.%f')]})
        # print(up_req)
        if form2.is_valid():
            # form2.date_out_time = (auto_now=True)
            f2 = form2.save(commit=False)
            userid = request.POST.get('uid')
            uid_value = Master.objects.filter(uid=userid).last()
            uid_name = uid_value.name
            ron = request.user
            rmn = ron.username
            '''try:
                f = Attende.objects.get(uid = userid)
            except Attende.DoesNotExist:
                return redirect('index')'''
            # if Attende.objects.get(uid=userid):
            # print(now.strftime('%Y-%m-%d %H:%M:%S.%f'))
            try:
                l = Attende.objects.filter(uid=userid, room_name=rmn).last()
                lpk = l.pk
                #print(lpk)

                now1 = datetime.datetime.now(IST)
                nvv = Attende.objects.filter(id=lpk, date=now1.strftime('%Y-%m-%d'), out_time__isnull=True)
                #print(nvv)
                if not nvv:
                    #print('l')
                    now1 = datetime.datetime.now(IST)
                    #f2.room_name = rmn
                    #f2.in_time = None
                    #f2.out_time = now1.strftime('%H:%M:%S.%f')
                    ot = now1.strftime('%H:%M:%S.%f')
                    Attende.objects.create(room_name=rmn, uid=userid, in_time=None, out_time=ot, uname=uid_name)
                    # f2.save()
                    messages.error(request, f'{uid_name} Your Recent IN is NOT FOUND')
                else:
                    for i in nvv:
                        #print(i)
                        nvvpk = i.pk
                        #print(nvvpk)

                    '''nv = Attende.objects.filter(uid=userid, room_name=rmn, out_time__isnull=True).last()
                    nvpk = nv.pk
                    print(nvpk)'''
                    # print(type(lpk))
                    # now.strftime('%Y-%m-%d %H:%M:%S.%f')
                    # datetime_NY.strftime("%Y-%m-%d %H:%M:%S.%f")
                    if nvvpk:
                        now1 = datetime.datetime.now(IST)
                        Attende.objects.filter(id=nvvpk).update(out_time=now1.strftime('%H:%M:%S.%f'))
                        messages.success(request, f'{uid_name} You are OUT')
                
            except:
                messages.error(request, 'Something went wrong. TRY AGAIN')

            # form2.save()
            return http.HttpResponseRedirect('')
            # form2.save()
            # Attende.objects.filter(fieldname="uid")
    

    context = {'form1': form1, 'form2': form2}
    return render(request, 'logging/index.html', context)


def details():
    data1 = Attende.objects.get(uid=userid)

@login_required
def attendence(request):
    return render(request, 'logging/attendence.html')

@login_required
def bydate(request):
    flag = 0
    obj = []
    if request.method == 'POST':
        fromdate = request.POST.get('fromd')
        #print(fromdate)
        todate = request.POST.get('tod')
        #print(todate)
        ron = request.user
        rmn = ron.username
        try:
            obj = Attende.objects.filter(date__range=[fromdate, todate], room_name=rmn)
            #print(obj)
            flag = 1
        except NotFound:
            print("InvalidDate")
    if len(obj) != 0:
        return render(request, 'logging/print.html', {'obj': obj, 'fromdate': fromdate, 'todate': todate, 'rmn': rmn})
    elif len(obj) == 0 and flag == 1:
        messages.error(request, 'No logs found')
    return render(request, 'logging/bydate.html')

@login_required
def id(request):
    form = AttendeFormOut()
    ud = []
    flag = 0
    if request.method == 'POST':
        form = AttendeFormOut(request.POST)
        if form.is_valid():
            userid = request.POST.get('uid')
            ron = request.user
            rmn = ron.username
            try:
                udetails = Attende.objects.filter(uid=userid, room_name=rmn)
                # print(udetails)
                ud = list(udetails)
                # print(ud)
                flag = 1
                '''for u in ud:
                    print(u.uid)
                for udetail in udetails:
                    ud = udetail
                    print(ud)
                    #print(udetail.uid)
                #print(udetails.uid)'''
            except NotFound:
                print("IDNotFound")

    # context = {'form': form, 'udetails': udetails}
    if len(ud) != 0:
        return render(request, 'logging/print.html', {'ud': ud, 'userid': userid, 'rmn': rmn})
    elif len(ud) == 0 and flag == 1:
        messages.error(request, 'No logs found')
    return render(request, 'logging/id.html')
    '''
                  {
                      'uid': udetails.uid,
                      'purpose': udetails.purpose,
                      'date_in_time': udetails.date_in_time,
                      'date_out_time': udetails.date_out_time
                  })'''

@login_required
def data_print(request):
    return render(request, 'logging/print.html')

@login_required
def intimate(request):
    return render(request, 'logging/intimate.html')

@login_required
def changepwd(request):
    return render(request, 'logging/changepwd.html')

@login_required
def auth_logout(request):
    logout(request)
    return redirect('auth_login')

def auth_login(request):
    form1 = CreateUserForm()
    #form2 = AttendeFormOut()

    if request.method == 'POST' and 'reg' in request.POST:

        form1 = CreateUserForm(request.POST)

        if form1.is_valid():
            form1.save()
            user = request.POST.get('username')
           
            
            '''if password != confirm_password:
                raise form1.ValidationError(
                    "password and confirm_password does not match"
                )
            profile = profile_form.save(commit=False)
            profile.user = user

            userid = profile_form.cleaned_data.get('uid')
            print(userid)
            profile.save()

            password = form1.cleaned_data.get('password1')
            print(password)
            user = authenticate(uid=uid, password=password)

            login(request, user)'''

            messages.success(request, 'Registration successful ' + user)
            return render(request, 'registration/login.html')
        else:
            password=request.POST.get('password1')
            confirm_password=request.POST.get('password2')
            if password != confirm_password:
                messages.error(request, "Password do not match")
            else:
                form1 = CreateUserForm()
                messages.error(request, "Unsuccessful registration. Invalid information.")

    if request.method == 'POST' and 'li' in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"You are now logged in as {username}.")
            return redirect('index')
        else:
            messages.error(request, "username or password is incorrect")

    context = {'form1': form1}
    return render(request, 'registration/login.html', context)

def register(request):
    return render(request, 'registration/register.html')
    '''form = UserCreationForm
    if request.method == 'POST':
        regForm = UserCreationForm(request.POST)

        if regForm.is_valid():
            regForm.save()
            messages.success(request, 'User has been registered!!!')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('')
    else:
        form = UserCreationForm()

    context = {'form': form}'''


#@csrf_exempt
def card_registrations(request):
    fm = SaveForm()
    #x=request.POST.get('uid')
    if request.method == 'POST':
        fm = SaveForm(request.POST)
        if fm.is_valid():
            fm.save()
    #context = {'fm': fm}
    return render(request, 'logging/card_reg.html')

class MasterViewSet(viewsets.ModelViewSet):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

    '''def get_queryset(self, *args, **kwargs):
        master_q = Master.objects.all()
        q = request.POST.get('rfid_id')
        return master_q'''

    @action(detail=False, methods=['POST'])
    def mget(self, request):
        if 'rfid_id' in request.data:

            rfid_id = request.data['rfid_id']
            rfid_value = Master.objects.filter(rfid_id=rfid_id).last()
            ruid = rfid_value.uid
            print(ruid)

            uid_value = Master.objects.filter(uid=ruid).last()
            uid_name = uid_value.name

            #user = request.user
            ron = request.user
            print('user ', ron)
            print("ru ", ron.username)

            # rfid_logout
            try:
                ao = Attende.objects.filter(room_name=ron.username, uid=ruid).last()
                print("try")
                print(ao)
                aopk = ao.pk
                print(aopk)
                now1 = datetime.datetime.now(IST)
                aov = Attende.objects.filter(id=aopk, date=now1.strftime('%Y-%m-%d'), out_time__isnull=True)
                print(aov)
                '''if not aov:
                    now1 = datetime.datetime.now(IST)
                    ot = now1.strftime('%H:%M:%S.%f')
                    Attende.objects.create(room_name=rmn, uid=userid, in_time=None, out_time=ot)
                    messages.error(request, 'Your LOGIN is in 404')
                else:'''
                for i in aov:
                    aovpk = i.pk
                print(aovpk)
                if aovpk:
                    now2 = datetime.datetime.now(IST)
                    Attende.objects.filter(id=aovpk).update(out_time=now2.strftime('%H:%M:%S.%f'))
                    #messages.success(request, 'You are OUT')
                    response = {'message': f'{uid_name} You are OUT'}
                else:
                    #messages.error(request, 'Your LOGIN is in 404')
                    response = {'message': f'{uid_name} Your IN is NOT FOUND'}

            # rfid_login
            except:
                print("except")
                now1 = datetime.datetime.now(IST)
                in_time = now1.strftime('%H:%M:%S.%f')
                a = Attende(room_name=ron.username, uid=ruid, in_time=in_time, uname=uid_name)
                a.save()
                #messages.success(request, 'You are IN')
                response = {'message': f'{uid_name} You are IN'}

            #response = {'message': 'rfid_id is posted successfully'}
            return Response(response, status=status.HTTP_200_OK)

        else:
            response = {'message': 'You need to provide your rfid_id'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        response = {'message': 'You cant update'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response = {'message': 'You cant create'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)




    @action(detail=False, methods=['POST'])
    def fp(self, request):
        if 'uid' in request.data:

            face_id = request.data['uid']

            uid_value = Master.objects.filter(uid=face_id).last()
            print(uid_value)
            uid_name = uid_value.name

            # user = request.user
            ron = request.user
            print('user ', ron)
            print("ru ", ron.username)

            # face_logout
            try:
                ao = Attende.objects.filter(room_name=ron.username, uid=face_id).last()
                print("try")
                print(ao)
                aopk = ao.pk
                print(aopk)
                now1 = datetime.datetime.now(IST)
                aov = Attende.objects.filter(id=aopk, date=now1.strftime('%Y-%m-%d'), out_time__isnull=True)
                print(aov)
                '''if not aov:
                    now1 = datetime.datetime.now(IST)
                    ot = now1.strftime('%H:%M:%S.%f')
                    Attende.objects.create(room_name=rmn, uid=userid, in_time=None, out_time=ot)
                    messages.error(request, 'Your LOGIN is in 404')
                else:'''
                for i in aov:
                    aovpk = i.pk
                print(aovpk)
                if aovpk:
                    now2 = datetime.datetime.now(IST)
                    Attende.objects.filter(id=aovpk).update(out_time=now2.strftime('%H:%M:%S.%f'))
                    # messages.success(request, 'You are OUT')
                    response = {'message': f'{uid_name} You are OUT'}
                else:
                    # messages.error(request, 'Your LOGIN is in 404')
                    response = {'message': f'{uid_name} Your IN is NOT FOUND'}

            # face_login
            except:
                print("except")
                now1 = datetime.datetime.now(IST)
                in_time = now1.strftime('%H:%M:%S.%f')
                a = Attende(room_name=ron.username, uid=face_id, in_time=in_time, uname=uid_name)
                a.save()
                # messages.success(request, 'You are IN')
                response = {'message': f'{uid_name} You are IN'}

            # response = {'message': 'rfid_id is posted successfully'}
            return Response(response, status=status.HTTP_200_OK)

        else:
            response = {'message': 'You need to provide your rfid_id'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)