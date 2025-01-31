from django.shortcuts import render
from basic_app.forms import userform,userprofileinfoform
# Create your views here.

#from django.core.urlresolvers import reverse # type: ignore
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse




def index(request):
    return render(request,'basic_app/index.html')

@ login_required
def special(request):
    return HttpResponse('you are login , nice')

@ login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



def register(request):

    registered = False

    if request.method == "POST":
        user_form = userform(data=request.POST)
        profile_form = userprofileinfoform(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.error_class)
        
    else:
        user_form= userform()
        profile_form = userprofileinfoform()
       
        
    return render(request,'basic_app/registration.html',
                 {'user_form':user_form,
                  'profile_form':profile_form,
                  'registered':registered} )






def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)


        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            
            else:
                return HttpResponse('account not active')
            
        else:
            print('someone tried to login and failed')
            print('username: {} and password: {}'.format(username,password))
            return HttpResponse('invalid login details supplied!')
    
    else:
        return render(request, 'basic_app/login.html')


