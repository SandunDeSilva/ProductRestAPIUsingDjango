from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from .models import Product
from rest_framework.exceptions import NotFound

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/product-list',
        'Detail view': '/product-detail/',
        'Create': '/product-create/',
        'Update': '/product-update/<int:id>',
        'Delete': '/product-detail/<int:id>',
    }

    return Response(api_urls)

@api_view(['GET'])
def ShowAll(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ViewProduct(request,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def CreateProduct(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def UpdateProduct(request,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# @api_view(['DELETE'])
# def DeleteProduct(request,pk):
#     product = Product.objects.get(id=pk)
#     product.delete()
        
#     return Response("Deleted Successfully!")

# @api_view(['GET'])
# def DeleteProduct(request, pk):
#     try:
#         product = Product.objects.get(id=pk)
#         product.delete()
#         return Response("Deleted Successfully!")
#     except Product.DoesNotExist:
#         raise NotFound("Product not found with id {}.".format(pk))

from rest_framework import status

@api_view(['DELETE'])
def DeleteProduct(request, pk):
    try:
        product = Product.objects.get(id=pk)
        product.delete()
        return Response("Deleted Successfully!")
    except Product.DoesNotExist:
        raise NotFound("Product not found with id {}.".format(pk))
