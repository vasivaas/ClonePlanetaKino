from django.shortcuts import render
from django.views.generic.base import View

from .models import Movies


class MoviesList(View):
    """
    Список фільмів
    """
    def get(self, request):
        movies = Movies.objects.all()
        return render(request, 'movies/movies.html', context={'movies_list': movies})