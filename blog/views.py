from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SignUpForm,LogInForm,Postform
from django.contrib import messages
from .models import Post
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group
# Home page
def home(request):
    posts=Post.objects.all().order_by('-id')
    return render(request,'blog/home.html',{'posts':posts})

# About page
def about(request):
    return render(request,'blog/about.html')

# Contact page
def contact(request):
    return render(request,'blog/contact.html')
   
 # Dashboard page
def dashboard(request):
    if request.user.is_authenticated:
        posts=Post.objects.all()
        user=request.user
        fullname=user.get_full_name;
        gps=user.groups.all()
        return render(request,'blog/dashboard.html',{'posts':posts,'fullname':fullname,'groups':gps})
    else:
        return HttpResponseRedirect('/login/')
# Logout page
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login/')

# Signup page
def user_signup(request):
    if request.method=='POST':
       fm=SignUpForm(request.POST);
       if fm.is_valid():
           user=fm.save()
           group=Group.objects.get(name='author')
           user.groups.add(group)
           messages.success(request,'Your account has been successfully Created..😍😍Aap ek blogger ban gye hai.❤')
    else:
        fm=SignUpForm()
    return render(request,'blog/signup.html',{'form':fm})
    
# Login page
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=LogInForm(request=request,data=request.POST);
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request,'Finally You Logged In successfull')
                    return HttpResponseRedirect('/dashboard/')
        else:
            fm=LogInForm()
        return render(request,'blog/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/');
#add new post
def addpost(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=Postform(request.POST)
            if fm.is_valid():
                title=fm.cleaned_data['title']
                desc=fm.cleaned_data['desc']
                pst=Post(title=title,desc=desc)
                pst.save()
                messages.success(request,'Your Post successfully uploaded..')
                # fm.Postform()
        else:
            fm=Postform()
        return render(request,'blog/addpost.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')

#update post
def updatepost(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Post.objects.get(pk=id)
            fm=Postform(request.POST ,instance=pi)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Your Post successfully updated..')
        else:
            pi=Post.objects.get(pk=id)
            fm=Postform(instance=pi)
        return render(request,'blog/updatepost.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')

#delete post
def deletepost(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            d=Post.objects.get(pk=id)
            d.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')

def user_contact(request):
    return render(request,'blog/contact.html')
    