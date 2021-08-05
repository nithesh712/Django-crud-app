# from django.shortcuts import render
from .models import BooksModel
from .serializer import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def BookList(request):
    booksobj = BooksModel.objects.all()
    serializer = BookSerializer(booksobj, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_book(request):
    # booksobj = BooksModel.objects.all()
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def update_book(request, id):
    booksobj = BooksModel.objects.get(id=id)
    serializer = BookSerializer(instance=booksobj, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_book(request, id):
    booksobj = BooksModel.objects.get(id=id)
    booksobj.delete()
    return Response('Book Deleted')
