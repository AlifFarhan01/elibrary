from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages



def login_user(request):
    if request.method == 'POST':
        print(request.POST)
        username_input = request.POST.get('username')
        password_input = request.POST.get('password')

        user = authenticate(username=username_input, password=password_input)

        if user is not None:
            login(request, user)      
            return redirect('katalog:index')  
        else:
            messages.error(request, 'Username atau password salah.')
    return render(request, 'login/index.html')

def logout_user(request):
    logout(request)
    messages.error(request, 'Berhasil Keluar')
    return redirect('login:login')


