from django.urls import path
# підключення відображень
from . import views

urlpatterns = [
    path('', views.MoviesList.as_view()),
]
