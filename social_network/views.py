from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate,logout,login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError
from .models import User,Post
from social_network.authentication import EmailBackend
from datetime import date
from django.utils.timezone import now


def post(request,id):

    if request.method == 'POST':
        post_message=request.POST.get('new_post')
        now_date=date
        img=request.FILES.get('img')
        post=Post(post_message=post_message,date=now_date,user=request.user,img=img)
        post.save()
        all_post=Post.objects.all().order_by('-date')
        return render(request,"social_network/index.html",{
            "all_post":all_post,
            "id":id,
        })
def index(request,id):

    return render(request,"social_network/index.html",{
        "id":id,
    })

def login_view(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
       # backend = EmailBackend()
        user=authenticate(request,email=email,password=password)
        print(user)
        if user is not None:
            login(request,user)
            print(user.id)
            return HttpResponseRedirect(reverse('index',args=[user.id]))
        else:
            return render(request,"social_network/login.html",{
                "message":"email or password error"
            })
    else:
        return render(request,"social_network/login.html")
        
    
def logout_view(request):

    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    if request.method=='POST':
        last_name=request.POST.get('prenom')
        first_name=request.POST.get('nom')
        password=request.POST.get('password')
        city=request.POST.get('ville')
        etat=request.POST.get('etat')
        email=request.POST.get('email')
        confirm=request.POST.get('confirm')
        if password!=confirm:
            return render(request,"social_network/register.html",{
                'message':"mot de passe error"
            })
        try:
            user=User(username=email,last_name=last_name,first_name=first_name,email=email,password=password,city=city,etat=etat)

            user.save()
        except IntegrityError:
             return render(request,"social_network/register.html",{
                'message':"user error"
            })
        login(request,user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request,"social_network/register.html")