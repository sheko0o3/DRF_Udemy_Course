from django.shortcuts import render

# Create your views here.

# CBV ViewSets
from rest_framework import viewsets


# CBV APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import UserProfile, ProfileFeedItem
from .serializers import HelloSerializer, UserProfileSerializer, ProfileFeedItemSerializer
from .permissions import UpdateOwnProfile, UpdateOwnStatus


from rest_framework.authentication import TokenAuthentication
from rest_framework import filters


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import BasicAuthentication

# CBV --> APIView
class HelloApiView(APIView):
    """Test API View"""
    serializer_class = HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response(data={'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response(data={'message': message})
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of object"""

        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({'method': 'DELETE'})


# CBV --> ViewSet

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = HelloSerializer

    def list(self, request):
        """Return a hello message."""
        return Response(data={"message": "Hello!"})

    def create(self, request):
        """Create a new hello message."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})

# ........................................................................ #
# .......................... Profile API ....................... #


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [UpdateOwnProfile]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "email"]


class UserLoginApiView(ObtainAuthToken):
   """Handle creating user authentication tokens"""

   renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ProfileFeedItemViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileFeedItemSerializer
    queryset = ProfileFeedItem.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (UpdateOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)




