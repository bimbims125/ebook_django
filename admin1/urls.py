from django.urls import path
from admin1 import views
urlpatterns = [
    path(r'admins/', views.admins, name='admins'),    
    path(r'admins/data_buku/', views.data_buku, name='data_buku'),
    path(r'admins/tambah_buku/', views.tambah_buku, name='tambah_buku'),
    path(r'admins/data_buku/detail_buku/<str:slug>', views.detail_buku, name='detail_buku'),
    path(r'admins/data_buku/filter/<str:slug>', views.genre_buku, name='genre_buku'),
    path(r'admins/edit_buku/<str:slug>', views.edit_buku, name='edit_buku'),
    path(r'admins/hapus_buku/<str:slug>', views.hapus_buku, name='hapus_buku'),
    path(r'admins/kategori/', views.kategori, name='kategori'),    
    path(r'admins/data_buku/search', views.search, name='search'),
    path(r'admins/kategori/<str:slug>', views.genre_detail,name='genre_detail')
]
