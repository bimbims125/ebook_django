from django.contrib.auth.models import Group
from django.shortcuts import render,redirect
from bookapp.models import *
from .forms import *
from django.contrib import messages
from admin1.decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth import authenticate, login, logout

# Create your views here.                                                                                                             
def home2(request):
    buku = Book.objects.all()
    total = Book.objects.all().count()
    kategori = Category.objects.all().count    
    konteks = {'buku':buku, 'total':total, 'kategori':kategori, }
    return render(request, 'index.html',konteks)

@unauthenticated_user
def registers(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')
        register_form = CreateUserForm(request.POST)
        
        if len(password) < 8:
            messages.warning(request,"Password setidaknya 8 karakter")
            
        if User.objects.filter(username=username).exists():
            messages.warning(request, "Username sudah digunakan, pakai username lain")
            
        if password != password2:
            messages.warning(request, 'Password tidak sama')                
            
        if register_form.is_valid():
            user = register_form.save()                        
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            messages.info(request, "Akun berhasil di buat")                    
            # msge = messages.info(request, "Akun gagal dibuat, coba lagi.")
    return render(request, 'registers.html', {'register_form':register_form,})

@unauthenticated_user
def logins(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request, username = username, password = password)
        if not user:
            messages.warning(request, "Invalid username or password")
        if user is not None:
            if user.groups.filter(name='admin').exists():
                login(request, user)
                return redirect('admins')
            else:
                login(request, user)
                return redirect('home')      
        else:
             pass
    return render(request, 'logins.html',)