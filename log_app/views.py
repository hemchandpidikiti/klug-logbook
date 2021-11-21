from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django import http
from .forms import AttendeFormIn, AttendeFormOut, CreateUserForm
from .models import Attende
import pytz
# from datetime import datetime
import datetime

#tz_NY = pytz.timezone('Asia/Kolkata')
# datetime_NY = datetime.now(tz_NY)
#IST = pytz.timezone('Asia/Kolkata')
#now1 = datetime.datetime.now(IST)
#print(now)


# temp = now.strftime('%Y-%m-%d %H:%M:%S.%f').replace(tzinfo=datetime.timezone.utc)

# Create your views here.
def index(request):
    # attende = Attende()
    form1 = AttendeFormIn()
    form2 = AttendeFormOut()
    IST = pytz.timezone('Asia/Kolkata')
    now1 = datetime.datetime.now(IST)

    if request.method == 'POST' and 'in' in request.POST:

        form1 = AttendeFormIn(request.POST)

        if form1.is_valid():
            #print(form1)
            form1.save()
            messages.success(request, 'You are IN')
            return http.HttpResponseRedirect('')
        else:
            print("form1 not found")
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
            userid = request.POST.get('uid')
            '''try:
                f = Attende.objects.get(uid = userid)
            except Attende.DoesNotExist:
                return redirect('index')'''
            # if Attende.objects.get(uid=userid):
            # print(now.strftime('%Y-%m-%d %H:%M:%S.%f'))
            try:
                l = Attende.objects.filter(uid=userid).last()
                lpk = l.pk
                # print(lpk)
                # print(type(lpk))
                # now.strftime('%Y-%m-%d %H:%M:%S.%f')
                # datetime_NY.strftime("%Y-%m-%d %H:%M:%S.%f")
                now1 = datetime.datetime.now(IST)
                Attende.objects.filter(id=lpk).update(out_time=now1.strftime('%H:%M:%S.%f'))
                messages.success(request, 'You are OUT')
            except InDoesNotExist:
                print("In required")

            # form2.save()
            return http.HttpResponseRedirect('')
            # form2.save()
            # Attende.objects.filter(fieldname="uid")
    context = {'form1': form1, 'form2': form2}
    return render(request, 'logging/index.html', context)


def details():
    data1 = Attende.objects.get(uid=userid)


def attendence(request):
    return render(request, 'logging/attendence.html')


def bydate(request):
    obj = []
    if request.method == 'POST':
        fromdate = request.POST.get('fromd')
        #print(fromdate)
        todate = request.POST.get('tod')
        #print(todate)
        try:
            obj = Attende.objects.filter(date__range=[fromdate, todate])
            #print(obj)
        except NotFound:
            print("InvalidDate")
    if len(obj) != 0:
        return render(request, 'logging/print.html', {'obj': obj, 'fromdate': fromdate, 'todate': todate})
    return render(request, 'logging/bydate.html')


def id(request):
    form = AttendeFormOut()
    ud = []
    if request.method == 'POST':
        form = AttendeFormOut(request.POST)
        if form.is_valid():
            userid = request.POST.get('uid')
            try:
                udetails = Attende.objects.filter(uid=userid)
                # print(udetails)
                ud = list(udetails)
                # print(ud)
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
        return render(request, 'logging/print.html', {'ud': ud, 'userid': userid})
    return render(request, 'logging/id.html')
    '''
                  {
                      'uid': udetails.uid,
                      'purpose': udetails.purpose,
                      'date_in_time': udetails.date_in_time,
                      'date_out_time': udetails.date_out_time
                  })'''


def print(request):
    return render(request, 'logging/print.html')

def intimate(request):
    return render(request, 'logging/intimate.html')

def changepwd(request):
    return render(request, 'logging/changepwd.html')

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

            '''profile = profile_form.save(commit=False)
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
            form1 = CreateUserForm()
            messages.error(request, "Unsuccessful registration. Invalid information.")

    if request.method == 'POST' and 'li' in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {username}.")
            return redirect('index')
        else:
            messages.info(request, "username or password is incorrect")

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

