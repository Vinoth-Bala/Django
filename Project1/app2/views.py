from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from .models import Person
import json 

# Create your views here.
@permission_classes((AllowAny,))
class userdetails(APIView):
    def get(self, request):
        data = Person.objects.filter(first_name='arun').values()
        
        return Response({'message': 'Data Retrived','Status':'Pass'},status=status.HTTP_200_OK)
        print(data)
    def post(self, request):
        data = Person.objects.create(
            
            first_name = 'su',
            last_name = 'KUMAR',
            ph_no = 123456,
            Blood_Group = 'o+v',
            )
        
        return Response(
            {
                'message': 'Data Retrived','Status':'Pass'
              

            },status=status.HTTP_200_OK

        )
