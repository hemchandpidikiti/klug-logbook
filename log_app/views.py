from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django import http
from .forms import AttendeFormIn, AttendeFormOut
from .models import Attende
import pytz
# from datetime import datetime
import datetime
import csv

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
            messages.error(request, 'ENTER CORRECT ID')
            #print("form1 not found")
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
            if userid:
                l = Attende.objects.filter(uid=userid).last()
                lpk = l.pk
                # print(lpk)
                # print(type(lpk))
                # now.strftime('%Y-%m-%d %H:%M:%S.%f')
                # datetime_NY.strftime("%Y-%m-%d %H:%M:%S.%f")
                now1 = datetime.datetime.now(IST)
                Attende.objects.filter(id=lpk).update(out_time=now1.strftime('%H:%M:%S.%f'))
                messages.success(request, 'You are OUT')
            else:
                messages.error(request, 'ID not exist')

            # form2.save()
            return http.HttpResponseRedirect('')
            # form2.save()
            # Attende.objects.filter(fieldname="uid")

    f = open(".\\static\\csv\\rfid.csv")
    csvreader = csv.reader(f)
    h = next(csvreader)
    #print(h)
    #rows = []
    #for row in csvreader:
        #rows.append(row)
    #messages.success(request, h)
    f.close()

    f1 = open(".\\static\\csv\\master.csv")
    csvreader = csv.reader(f1)
    h1 = next(csvreader)
    for i in h:
        k = i
    rows = []
    for r in csvreader:
        #r = row[0].split('\t')
        if r[0] == k:
            rows.append(r[1])
    for row in rows:
        messages.success(request, row)
    f1.close()

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