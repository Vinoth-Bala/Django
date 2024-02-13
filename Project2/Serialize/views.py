from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from .models import students,Department
from Serialize.serializer import stu_serializer,dept_serializer
import json 


# Create your views here.
@permission_classes((AllowAny,))
class StuDetails(APIView):
    def get(self, request):
        data = students.objects.all()
        stu = stu_serializer (data,many=True)
        return Response({'message': 'Data Retrived','Status':'Pass','Data':stu.data},status=status.HTTP_200_OK)
    
    def post(self,request):
        data1 =stu_serializer(data=request.data)
        
        if data1.is_valid():
            data1.save()
            return Response({'message': 'Data Retrived','Status':'Pass','Data':data1.data},status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Error','Status':'Pass','Data':data1.data},status=status.HTTP_404_NOT_FOUND)

    def put(self,request):
        datas=request.data.get("id")
        try:
            data=students.objects.get(id=datas)
            data1=stu_serializer(data,data=request.data)
            if data1.is_valid():
                data1.save()
                return Response({'message':"Data retrived",'Status': 'pass','data':data1.data},status=status.HTTP_200_OK)
            else:
              return Response({'message':"error returned",'Status': 'pass','data':data1.data},status=status.HTTP_200_OK)                       
        except:
            return Response({'message':"error returned",'Status': 'failed'},status=status.HTTP_404_NOT_FOUND)           
    
    def delete(self,request):
        datas=request.data.get("id")
        try:
            data=students.objects.get(id=datas)
        except:
            return Response({'message':"error returned",'Status': 'failed'},status=status.HTTP_404_NOT_FOUND)
        data.delete()
        return Response({'message':"Data Deleted",'Status': 'pass'},status=status.HTTP_200_OK)
    






@permission_classes((AllowAny,))
class DepDetails(APIView):
    def get(self, request):
        data = Department.objects.all()
        return Response({'message': 'Data Retrived','Status':'Pass','Data':Dep.data},status=status.HTTP_200_OK)
    
    def post(self,request):
        data1 =dept_serializer(data=request.data)
        
        if data1.is_valid():
            data1.save()
            return Response({'message': 'Data Retrived','Status':'Pass','Data':data1.data},status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Error','Status':'Pass','Data':data1.data},status=status.HTTP_404_NOT_FOUND)
        
    def put(self,request):
        datas=request.data.get("id")
        try:
            data=Department.objects.get(id=datas)
            data1=dept_serializer(data,data=request.data)
            if data1.is_valid():
                data1.save()
                return Response({'message':"Data retrived",'Status': 'pass','data':data1.data},status=status.HTTP_200_OK)
            else:
              return Response({'message':"error returned",'Status': 'pass','data':data1.data},status=status.HTTP_200_OK)                       
        except:
            return Response({'message':"error returned",'Status': 'failed'},status=status.HTTP_404_NOT_FOUND)           
    
    def delete(self,request):
        datas=request.data.get("id")
        try:
            data=Department.objects.get(id=datas)
        except:
            return Response({'message':"error returned",'Status': 'failed'},status=status.HTTP_404_NOT_FOUND)
        data.delete()
        return Response({'message':"Data Deleted",'Status': 'pass'},status=status.HTTP_200_OK)

        

    
