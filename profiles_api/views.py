from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

# Create your views here.

class HelloApiView(APIView):

    serializer_class=serializers.HelloSerializer

    """Test API View  """
    def get(self,request,format=None):
        """ Returns a list of APIView features"""
        apiview=['this','is','a','list','of','elements']
        return Response({'message':'hello!','an_apiview':apiview})


    def post(self,request):
        """create a hello message with name"""
        serializer=self.serializer_class(data=request.data)

        if(serializer.is_valid()):
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """Handle a partial update of an object i.e update fields provided"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """Handle delete"""
        return Response({'method':'DELETE'})




class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class=serializers.HelloSerializer

    def list(self,request):
        """Return a hello message"""

        a_viewset=[
        'Uses actions(list, create, retrieve, update,partial_update)',
        'Automatically maps to urls using routers',
        'less code'
        ]
        return Response({'message':'Hello!','a_viewset':a_viewset})


    def create(self,request):
        """create a new hello message"""
        serializer=self.serializer_class(data=request.data)

        if(serializer.is_valid()):
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )


    def retrieve(self,request,pk=None):
        """handle getting an object by its id"""
        return Response({'hhtp_method':'GET'})

    def update(self,request,pk=None):
        """handle updating a object"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """handle updatingpart of  a object"""
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """handle removing a object"""
        return Response({'http_method':'DELETE'})




class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    Permission_classes=(permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email',)



class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES
