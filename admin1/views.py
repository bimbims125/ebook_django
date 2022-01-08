from django.shortcuts import redirect, render
from admin1.decorators import unauthenticated_user, allowed_users
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, forms, login, logout

from admin1.forms import AddBookForm
from .decorators import allowed_users, unauthenticated_user, admin_only

# Import models
from bookapp.models import *
from .context_processor import *

print
# Create your views here.
@login_required(login_url='logins')
@allowed_users(allowed_roles=['admin'])
def admins(request):
    total_buku = Book.objects.all().count()
    total_kategori = Category.objects.all().count()
    user_total = User.objects.all().count()
    kategori = Category.objects.all()
    # koding = Book.objects.filter(category__name='Coding').count()    
    konteks = {'total_buku':total_buku, 'total_kategori':total_kategori,'user_total':user_total, 'kategori':kategori, }
    return render(request, 'content/index.html', konteks)

@login_required(login_url='logins')
@allowed_users(allowed_roles=['admin'])
def logout_admin(request):
    logout(request)
    return redirect('logins')
# =========== Create Read Update Delete =========== 
@login_required(login_url='logins')
@allowed_users(allowed_roles=['admin'])
def data_buku(request):
    buku = Book.objects.all()
    kategori = Category.objects.all()
    konteks = {'buku':buku, 'kategori':kategori}
    return render(request, 'content/data_buku.html',konteks)

@login_required(login_url='logins')
@allowed_users(allowed_roles=['admin'])
def kategori(request):
    kategori = Category.objects.all()
    konteks = {'kategori':kategori}
    return render(request, 'content/kategori.html', konteks)

@login_required(login_url='logins')
@allowed_users(allowed_roles=['admin'])
def kategori(request):
    kategori = Category.objects.all()
    konteks = {'kategori':kategori}
    return render(request, 'content/kategori.html', konteks)

@login_required(login_url='logins')
@allowed_users(allowed_roles=['admin'])
def detail_buku(request, slug):
    buku = Book.objects.get(slug=slug)
    konteks = {'buku':buku}
    return render(request, 'crud/detail_buku.html', konteks)

@login_required(login_url='logins')
@allowed_users(allowed_roles=['admin'])
def tambah_buku(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST, request.FILES)        
        if form.is_valid():
            form.save()
            messages.info(request, "Buku berhasil ditambahkan!")
            return redirect('data_buku')   
        else:
            messages.danger(request, "Buku gagal di edit")            
    else:
        form = AddBookForm()     
        
    return render(request, 'crud/tambah_buku.html', {'form':form,'messages':messages})

@login_required(login_url='logins')
@allowed_users(allowed_roles=['admin'])
def edit_buku(request, slug):
    buku = Book.objects.get(slug=slug)
    
    if request.method == 'POST':
        form = AddBookForm(request.POST or None, request .FILES or None, instance=buku)        
        if form.is_valid():
            form.save()
            form = AddBookForm(instance=buku)
            messages.success(request, "Buku berhasil di edit")
            return redirect('data_buku')
    else:
        form = AddBookForm(instance=buku)
    return render(request, 'crud/edit_buku.html',{'buku':buku,'form':form,'messages':messages})

@login_required(login_url='logins')
@allowed_users(allowed_roles=['admin'])
def hapus_buku(request, slug):
    buku = Book.objects.get(slug=slug)
    buku.delete()
    messages.info(request, "Buku Berhasil dihapus")
    return redirect('data_buku')

@login_required(login_url='logins')
@allowed_users(allowed_roles=['admin'])
def search(request):
    searched_books = Book.objects.filter(title__icontains = request.POST.get('name_of_book'))
    kategori = Category.objects.all()
    total_bk = searched_books.count()
    return render(request, 'content/search.html', {'searched_books':searched_books, 'total_bk':total_bk, 'kategori':kategori})

@login_required(login_url='logins')
@allowed_users(allowed_roles=['admin'])
def genre_detail(request, slug):
    genre = Category.objects.get(slug=slug)
    return render(request, 'crud/detail_genre.html',{'genre_detail':genre})

@login_required(login_url='logins')
@allowed_users(allowed_roles=['admin'])
def genre_buku(request, slug):
    genre = Category.objects.get(slug=slug)
    kategori = Category.objects.all()
    return render(request, 'content/book_genre.html',{'genre_detail':genre,'kategori':kategori})

    
    