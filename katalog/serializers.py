from rest_framework import serializers
from .models import Buku, Peminjaman

class BukuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buku
        fields = '__all__'

class PeminjamanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peminjaman
        fields = '__all__'