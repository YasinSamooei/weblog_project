# imports
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from .forms import LoginForm , EditForm
#------------------------------------------------------------------------------------------------------------------


# login
def user_login (request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            user= User.objects.get(username=form.cleaned_data.get('username'))
            login(request,user)
            return redirect('/')
    else:
        form=LoginForm()
    return render(request , "acount_app/login.html" , {"form":form})

        #بر اساس قالب html
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # user = authenticate(request , username = username , password = password)
        # if user is not None:
        #     login(request , user)
        #     return redirect('/')
#------------------------------------------------------------------------------------------------------------------


    
# logout    
def user_logout(request):
    logout(request)
    return redirect('/')
#------------------------------------------------------------------------------------------------------------------


# register
def user_register(request):
    context = {"errors":[]}
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            context['errors'].append("passwords are not same")
            return render(request , 'acount_app/register.html' , context)
        user = User.objects.create(username=username , email=email , password = password1)
        login(request , user)
        return redirect('/')
    return render(request , 'acount_app/register.html')
#------------------------------------------------------------------------------------------------------------------



# edit_profile
def edit_profile(request):
    user = request.user
    form = EditForm(instance=user)
    if request.method=="POST":
        form=EditForm(instance=user,data=request.POST)
        if form.is_valid():
            form.save()
    return render(request,"acount_app/edit.html",{"form":form})