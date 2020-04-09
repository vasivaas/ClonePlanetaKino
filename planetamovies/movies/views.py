from django.shortcuts import render
from django.views.generic.base import View

from .models import Movies, Slider


class MoviesList(View):
    """
    Список фільмів для головної сторінки сайту
    """
    def get(self, request):
        movies_coming_soon = Movies.objects.filter(status__exact='c')
        coming_soon_count = Movies.objects.filter(status__exact='c').count()
        to_view_movies = Movies.objects.filter(status__exact='t').count()
        slider = Slider.objects.order_by('index').all()
        return render(request, 'movies/index.html', context={'movies_list': movies_coming_soon,
                                                              'num_coming_soon': coming_soon_count,
                                                              'now_view_movies': to_view_movies,
                                                              'slider': slider})

