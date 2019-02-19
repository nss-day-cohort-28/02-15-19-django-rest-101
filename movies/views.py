from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import filters

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

  # Shorthand version of the get_queryset override below
  # https://www.django-rest-framework.org/api-guide/filtering/
  filter_backends = (filters.SearchFilter,)
  search_fields = ('title','year')

  # def get_queryset(self):
  #   query_set = Movie.objects.all()
  #   keyword = self.request.query_params.get('search', None)
  #   if keyword is not None:
  #     print("query params", keyword)
  #     query_set = query_set.filter(title__icontains=keyword)
  #   return query_set

class DirectorViewSet(viewsets.ModelViewSet):
  queryset = Director.objects.all()
  serializer_class = DirectorSerializer
