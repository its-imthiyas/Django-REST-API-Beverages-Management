from django.core.serializers import serialize
from django.http import JsonResponse
from .models import Beverage
from .serializers import BeverageSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def beverage_list(request, format = None):

    if request.method =='GET':
        beverages = Beverage.objects.all()
        serializer = BeverageSerializer(beverages, many=True)
        return Response(serializer.data)

    if request.method=='POST':
        serializer = BeverageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def beverage_detail(request, id, format = None):
    try:
        beverage = Beverage.objects.get(pk=id)
    except Beverage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BeverageSerializer(beverage)
        return Response(serializer.data) 
    elif request.method == 'PUT':
        serializer = BeverageSerializer(beverage, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        beverage.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)