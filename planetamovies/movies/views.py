from django.shortcuts import render
from django.views.generic.base import View

from .models import Movies


class MoviesList(View):

    def get_movie(self, request):
        movies = Movies.objects.all()

        return render(request, 'movies/movies.html', context={'movies': movies})