from django.shortcuts import render,redirect
from .forms import UserSignupForm,UserLoginForm
from .models import Chef
from django.contrib.auth import authenticate,login


def login_user(request):
    #when user is submitting the form
    if request.method=="POST":
        formdata=UserLoginForm(request.POST)
        if formdata.is_valid():

            #get the data fields
            username=formdata.cleaned_data["username"]
            password=formdata.cleaned_data["password"]
            
            #fill the data fields
            chef = authenticate(request,username=username,password=password)
            print(chef)
            if chef:
                login(request,chef)

            #after creation, redirect to login page
            #return redirect("")
    
    #add validations later
    userform=UserLoginForm()
    context={
        "form":userform
    }
    return render(request,"chef/login.html",context)


def signup_user(request):
    #when user is submitting the form
    if request.method=="POST":
        formdata=UserSignupForm(request.POST)
        if formdata.is_valid():

            #get the data fields
            username=formdata.cleaned_data["username"]
            fname=formdata.cleaned_data["first_name"]
            lname=formdata.cleaned_data["last_name"]
            profile_picture=formdata.cleaned_data["profile_picture"]
            password=formdata.cleaned_data["password"]

            #fill the data fields
            chef = Chef.objects.create_user(username=username,password=password)
            chef.first_name=fname
            chef.last_name=lname
            chef.profile_picture=profile_picture
            chef.save()

            #after creation, redirect to login page
            return redirect("")
    
    #when user requesting signup page
    userform=UserSignupForm()
    context={
        "form":userform
    }
    return render(request,"chef/signup.html",context)
