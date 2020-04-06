from django.contrib import admin

from .models import Category, ActorDirector, Genre, Movies, MoviesPicture, StarRate, Rate, Reviews

admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(ActorDirector)
admin.site.register(Movies)
admin.site.register(MoviesPicture)
admin.site.register(Rate)
admin.site.register(StarRate)
admin.site.register(Reviews)
