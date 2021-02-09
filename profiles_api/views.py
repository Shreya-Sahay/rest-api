from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


from profiles_api import serializer
from profiles_api import models
from profiles_api import permissions




class HelloApiView(APIView):
    '''Test API VIEW'''
    serializer_class = serializer.HelloSerializer
    def get(self, request, format=None):
        '''Retur A list of apiview features and creating list of information'''
        an_apiview = [
            'uses HTTP methods as function (get, post, put, delete)',
            'Is similar to a traditional DJANGO View',
            'Gives you most control over your applivation logic',
            'Is mapped manually to URLS',
         ]
        return Response({'message': 'Hello!', 'an_apiview':an_apiview})
        
    def post(self, request):
        '''Create a hello message with out name'''
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, 
                status = status.HTTP_400_BAD_REQUEST
            )
    def put(self, request, pk=None):
        """hANDLE updating an object"""
        return Response({'method':'PUT'})
        
    def patch(self, request, pk=None):
        """handle a partial update of an object"""
        return Response({'method': 'PATCH'})
        
    def delete(self, request, pk=None):
        """delete an object"""
        return Response({'method': 'DELETE'})
        
        
class HelloViewSet(viewsets.ViewSet):
    '''Test API ViewSet'''
    serializer_class = serializer.HelloSerializer
    def list(self,request):
        '''Return a hello Message'''
        a_viewset = [
            'Uses actions (list, create,retrieve, update partial_updat)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]
        
        
        return Response({'message':'Hello!', 'a_viewset':a_viewset})
        
    def create(self, request):
        '''Create a new hello message'''
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                    )
                    
    def retrieve(self, request, pk=None):
        '''Hnadle getting an object by its ID'''
        return Response({'http_method':'GET'})
      
    def update(self, request, pk=None):
        '''Handle updating an object'''
        return Response({'http_method': 'PUT'})
        
    def partial_update(self, request, pk=None):
        '''Handle updating  part an object'''
        return Response({'http_method': 'PATCH'})
        
    def destroy(self, request, pk=None):
        '''Handle removing an object'''
        return Response({'http_method': 'DELETE'})
        
        
class UserProfileViewSet(viewsets.ModelViewSet):
    '''Handle creating and updating objects'''
    serializer_class = serializer.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)
    
class UserLoginApiView(ObtainAuthToken):
    '''Handle creating user authentucation tokens'''
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    