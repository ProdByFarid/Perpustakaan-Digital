from django.urls import path
from . import views

urlpatterns = [
    path('buku/', views.api_buku_list, name='api_buku_list'),
    path('buku/<int:pk>/', views.api_buku_detail, name='api_buku_detail'),
    
    # Tambahkan baris ini untuk URL Peminjaman:
    path('peminjaman/', views.api_peminjaman_list, name='api_peminjaman_list'),
]