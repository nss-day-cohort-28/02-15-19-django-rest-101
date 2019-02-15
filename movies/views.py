from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from movies.models import Movie, Director
from movies.serializers import MovieSerializer, DirectorSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'movies': reverse('movies', request=request, format=format),
        'directors': reverse('directors', request=request, format=format)
    })

class MovieViewSet(viewsets.ModelViewSet):
  queryset = Movie.objects.all()
  serializer_class = MovieSerializer

class DirectorViewSet(viewsets.ModelViewSet):
  queryset = Director.objects.all()
  serializer_class = DirectorSerializer
