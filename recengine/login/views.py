from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from forms import UserForm,CustomCreateUserForm
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
def home(req): 
    return  render_to_response("home_1.html")
def regist(req):
    if req.method == 'POST':
        uf = CustomCreateUserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password1']
            email = uf.cleaned_data['email']
            user = User.objects.create_user(username = username, password = password,email=email)
            user.save()
            return HttpResponseRedirect('/login/')
    else:
        uf = CustomCreateUserForm()
    return render_to_response('regist.html', {'uf': uf})


def login(request):
    uf = UserForm(request.POST)
    if request.user.is_authenticated():
        return HttpResponseRedirect('/app1/table')
    if request.method == 'POST':
        print request.POST

        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #users = User.objects.filter(username__exact = username, password__exact = password)
            user1 = authenticate(username=username, password=password)
            #if user:
            if user1 is not None and user1.is_active:
                response = HttpResponseRedirect('/app1/dashboard/')
                #response.set_cookie('username', username, 3600)
                auth_login(request,user1)
                return response
            else:
                return HttpResponseRedirect('/login/')
    return render_to_response('login.html', {'uf': uf})

def index(request):
    if  request.user.is_authenticated():
        username = request.user
        return render_to_response('log-index.html', {'username': username})
    return render_to_response('/login/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
