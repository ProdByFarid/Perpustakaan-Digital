from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Buku, Peminjaman
from .serializers import BukuSerializer, PeminjamanSerializer

@api_view(['GET', 'POST'])
def api_buku_list(request):
    if request.method == 'GET':
        buku = Buku.objects.all()
        serializer = BukuSerializer(buku, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BukuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def api_buku_detail(request, pk):
    try:
        buku = Buku.objects.get(pk=pk)
    except Buku.DoesNotExist:
        return Response({'error': 'Buku tidak ditemukan'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BukuSerializer(buku)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BukuSerializer(buku, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        buku.delete()
        return Response({'message': 'Buku berhasil dihapus'}, status=status.HTTP_204_NO_CONTENT)

# --- FUNGSI UNTUK PEMINJAMAN ---
@api_view(['GET', 'POST'])
def api_peminjaman_list(request):
    if request.method == 'GET':
        peminjaman = Peminjaman.objects.all()
        serializer = PeminjamanSerializer(peminjaman, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PeminjamanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)