from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status 
from mywebApp2.models import StudentDetails,StudentDetails1
from mywebApp2.serializers import SdSerializer,SdSerializer1
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def sddetails_list(request):
    # GET list of users, POST a new user, DELETE  user
    if request.method == 'GET':
        sddetails = StudentDetails.objects.all() 
               
        sddetails_serializer = SdSerializer(sddetails, many=True)
        return JsonResponse(sddetails_serializer.data, safe=False)
        # 'safe=False' for objects serialization
        
    elif request.method == 'POST':
        sddetails_data = JSONParser().parse(request)
        sddetails_serializer = SdSerializer(data=sddetails_data)
        if sddetails_serializer.is_valid():
            sddetails_serializer.save()
            return JsonResponse(sddetails_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(sddetails_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def sddetails_detail(request, pk):
    # find user by pk (id)
    sddetails = StudentDetails.objects.get(pk=pk)
    if request.method == 'GET': 
        sddetails_serializer = SdSerializer(sddetails) 
        return JsonResponse( sddetails_serializer.data) 
    elif request.method == 'PUT': 
         sddetails_data = JSONParser().parse(request) 
         sddetails_serializer = SdSerializer(sddetails, data=sddetails_data) 
         if sddetails_serializer.is_valid(): 
              sddetails_serializer.save() 
              return JsonResponse(sddetails_serializer.data) 
         return JsonResponse(sddetails_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE':
       sddetails.delete()
       return JsonResponse({'message': 'Student Details was deleted successfully!'}, 
        status=status.HTTP_204_NO_CONTENT
        )

def sddetails_delete(request, pk):
    
    # find product by pk (id)
    
   sddetails = StudentDetails.objects.get(pk=pk)



def sddetails_list1(request):
    # GET list of users, POST a new user, DELETE  user
    if request.method == 'GET':
        sddetails1 = StudentDetails1.objects.all() 
               
        sddetails_serializer1 = SdSerializer1(sddetails1, many=True)
        return JsonResponse(sddetails_serializer1.data, safe=False)
        # 'safe=False' for objects serialization
        
    elif request.method == 'POST':
        sddetails_data1 = JSONParser().parse(request)
        sddetails_serializer1 = SdSerializer1(data=sddetails_data1)
        if sddetails_serializer1.is_valid():
            sddetails_serializer1.save()
            return JsonResponse(sddetails_serializer1.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(sddetails_serializer1.errors, status=status.HTTP_400_BAD_REQUEST)

def sddetails_detail1(request, pk):
    # find user by pk (id)
    sddetails1 = StudentDetails1.objects.get(pk=pk)
    if request.method == 'GET': 
        sddetails_serializer1 = SdSerializer1(sddetails1) 
        return JsonResponse( sddetails_serializer1.data) 
    elif request.method == 'PUT': 
         sddetails_data1 = JSONParser().parse(request) 
         sddetails_serializer1 = SdSerializer(sddetails1, data=sddetails_data1) 
         if sddetails_serializer1.is_valid(): 
              sddetails_serializer1.save() 
              return JsonResponse(sddetails_serializer1.data) 
         return JsonResponse(sddetails_serializer1.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE':
       sddetails.delete1()
       return JsonResponse({'message': 'Student Details was deleted successfully!'}, 
        status=status.HTTP_204_NO_CONTENT
        )

def sddetails_delete1(request, pk):
    
    # find product by pk (id)
    
   sddetails1 = StudentDetails1.objects.get(pk=pk)


