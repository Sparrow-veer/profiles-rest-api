from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):

    """Test API View  """
    def get(self,request,format=None):
        """ Returns a list of APIView features"""
        apiview=['this','is','a','list','of','elements']
        return Response({'message':'hello!','an_apiview':apiview})
