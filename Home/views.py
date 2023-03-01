from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from Home.models import Entry,user
from django.views.decorators.cache import cache_control
from requests import request


# Create your views here.
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def login(request):
    if request.method=="POST":
        userid = request.POST['LOGIN_ID']
        password = request.POST['PASSWORD']
        request.session['userid'] = userid
        if len(userid)<8 or len(password)<8:
            return render(request,"login.html")
        else:
            request.session['userid']=userid
            if user.objects.filter(Userid=userid):
                for data1 in user.objects.filter(Userid=userid):
                    user1 = data1.Userid
                    pswd = data1.Password
                if user1 == userid and pswd == password:
                    for data2 in user.objects.filter(Userid=user1):
                        user2 = data2.Userid
                    return render(request,"home.html",{'user2':user2})
                else:
                    return render(request,"login.html")
            else:
                return render(request,"login.html")
    else:
        return render(request,"login.html")

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def registeration(request):
    arr1=['!','@','#','$','%','^','&','*']
    count=0
    if request.method=="POST":
        userid = request.POST['LOGIN_ID']
        password = request.POST['PASSWORD']
        for i in arr1:
            if i in password:
                if len(userid)<8 or len(password)<8:
                    return render(request,"registeration.html")
                else:
                    user(Userid = userid,Password = password).save()
                    return render(request,"login.html")
            else:
                count+=1
        if count==len(arr1):
            return render(request,"registeration.html")
    else:
        return render(request,"registeration.html")

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def logout(request):
    if 'userid' in request.session:
        print(request.session['userid'])
        del request.session['userid']
        logout(request)
        #print(request.session['userid'])
    return render(request,"logout.html")

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def home(request):
    if 'userid' in request.session:
        user2 =  request.session['userid']
        if request.method=="GET":
            user2 = user2
        return render(request,"home.html",{'user2':user2})
            
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def show(request):
    # user2 = request.GET["login_id"]
    user2 =  request.session['userid']
    data = Entry.objects.filter(USERID=user2)
    return render(request,"show.html",{'data':data})

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def send(request):
    if request.method == "POST":
        USERID = request.POST['login_id']
        NAME = request.POST['name']
        SURNAME = request.POST['surname']
        Entry(NAME = NAME,SURNAME = SURNAME,USERID=USERID).save()
        msg = "data stored sucessfully"
        return render(request,"home.html",{'msg':msg,'user2':USERID})
    else:
        return HttpResponse("<h1>error - 404 NOT FOUND</h1>")
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def delete(request):
    ID = request.GET['id']
    Entry.objects.filter(ID=ID).delete()
    return HttpResponseRedirect("show")
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def edit(request):
    ID = request.GET['id']
    NAME=SURNAME="NOT AVAILABE"
    for data in Entry.objects.filter(ID=ID):
        ID = data.ID
        NAME=data.NAME
        SURNAME=data.SURNAME
    return render(request,'edit.html',{'ID':ID,'NAME':NAME,'SURNAME':SURNAME})
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def RecordEdited(request):
    if request.method=="POST":
        ID = request.POST['id']
        NAME = request.POST['name']
        SURNAME = request.POST['surname']
        Entry.objects.filter(ID=ID).update(NAME=NAME,SURNAME=SURNAME)
        return HttpResponseRedirect("show")
    else:
        HttpResponse("<h1>page not found</h1>")