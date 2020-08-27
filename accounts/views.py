from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1']
            )
            login(request,user)
            return redirect('read_blog_list')
        else:
            return render(request, 'accounts/signup.html')
    else:
        return render(request, 'accounts/signup.html')

def signin(request):
    #authenticate
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username =username, password=password)
        #login 성공
        if user is not None:
            login(request, user)
            return redirect('read_blog_list')
        #다시 login화면으로
        else :
            return render(request, 'accounts/signin.html', {'error':'incorrect ID or password'})
    else:
        return render(request, 'accounts/signin.html')

def signout(request):
    logout(request)
    return redirect('read_blog_list')