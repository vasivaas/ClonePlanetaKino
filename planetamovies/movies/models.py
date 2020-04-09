from django.db import models
from datetime import date


# Create your models here.
class BaseModel(models.Model):
    """
    Абстрактна модель, де ми явно передаєм в django поле objects
    """
    objects = models.Manager()
    class Meta:
        abstract = True


class Category(BaseModel):
    '''
        Модель Категорій
    '''

    # model fields
    name = models.CharField('Назва', max_length=65)
    describe = models.TextField('Опис')
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


    # class Meta for model (this container have a meta data)
    class Meta:
        # імя моделі в однині
        verbose_name = 'Категорія'
        # імя моделі в множині
        verbose_name_plural = 'Категорії'


class ActorDirector(BaseModel):
    """
    Модель Режисерів та акторів
    """
    name = models.CharField("Ім'я", max_length=50)
    age = models.PositiveSmallIntegerField('Вік', default=0, help_text='Кількість повних років')
    describe_text = models.TextField('Опис про актора/директора')
    image = models.ImageField(upload_to='picture/%Y/%m/%d/', max_length=200, unique=True, help_text='Зображення актора/режисера')


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Актор/Режисер'
        verbose_name_plural = 'Актори/Режисери'


class Genre(BaseModel):
    """
    Модель Жанрів
    """
    name = models.CharField("Ім'я", max_length=50)
    describe_text = models.TextField('Опис жанру')
    url = models.SlugField(max_length=100, unique=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанри'


class Movies(BaseModel):
    """
    Модель фільму
    """
    objects = models.Manager()
    name = models.CharField('Назва', max_length=65)
    tagline = models.CharField('Девіз до фільму', max_length=65, null=True, unique=True, blank=True)
    describe_text = models.TextField('Опис Фільму')
    poster_img = models.ImageField(upload_to='poster/%Y/%m/%d/',  max_length=200, unique=True, help_text='Зображення постера для фільму')
    year = models.PositiveSmallIntegerField('Дата виходу', default=2020, help_text='Введіть рік виходу фільму в прокат')
    country = models.CharField('Країна', max_length=25)
    director = models.ManyToManyField(ActorDirector, verbose_name='режисер', related_name='film_director', help_text='Вибрати Режисера(-ів) для фільму')
    actor = models.ManyToManyField(ActorDirector, verbose_name='актори', related_name='film_actor', help_text='Вибрати Актора(-ів) для фільму')
    genre = models.ManyToManyField(Genre, verbose_name='жанри', help_text='Вибрати Жанри для фільму')
    world_premier = models.DateField("Прем'єра в світі", default=date.today)
    movie_budget = models.PositiveSmallIntegerField('Виділений бюджет на фільм', default=0, help_text='Вказати суму в долларах')
    earnings_world = models.PositiveSmallIntegerField('Отримано грошей в світі', default=0, help_text='Вказати суму в долларах')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=100, unique=True)

    MOVIE_STATUS = (
        ('c', 'Скоро в прокаті'),
        ('n', 'Новинки'),
        ('t', 'Зараз у прокаті'),
        ('a', 'Всі фільми'),
    )
    status = models.CharField(max_length=1, choices=MOVIE_STATUS, blank=True, default='a', help_text='Статус фільму, для відфільтровки записів')
    age_rest = models.PositiveSmallIntegerField("Вікові обмеження", default=0)
    MOVIE_EXPANSIVE = (
        ('2D', 'В 2D'),
        ('3D', 'В 3D'),
        ('4D', 'В 4D'),
    )
    expanse = models.CharField(max_length=2, choices=MOVIE_EXPANSIVE, blank=True, default='2D', help_text="В якому розширенні можна подивитись(2D, 3D, 4D)")
    MOVIE_TECHNOLOGY = (
        ('Cintech+', 'Cintech+'),
        ('Imax', 'Imax'),
    )
    technology = models.CharField(max_length=10, choices=MOVIE_TECHNOLOGY, blank=True, default='Cintech+', help_text="Технологія в якій показують фільм")
    draft = models.BooleanField('Чорновик', default=False)

    def __str__(self):
        return self.name

    def display_director(self):
        return ', '.join([director.name for director in self.director.all()])

    display_director.short_description = 'ActorDirector'

    def display_actor(self):
        return ', '.join([actor.name for actor in self.actor.all()])

    display_actor.short_description = 'ActorDirector'

    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre.all()])

    display_genre.short_description = 'Genre'

    class Meta:
        verbose_name = 'Фільм'
        verbose_name_plural = 'Фільми'


class MoviesPicture(BaseModel):
    """
    Модель картинок з фільму
    """
    name = models.CharField('Назва для кадру', max_length=65)
    describe_text = models.TextField('Опис до кадру з фільму')
    images = models.ImageField(upload_to='movies/picture/%Y/%m/%d/',  max_length=200, unique=True, help_text='Зображення постера для фільму')
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, verbose_name='Фільм')
    #Cascade - видаліть усі фото якщо видалити звязаний фільм


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Кадр з фільму'
        verbose_name_plural = 'Кадри з фільму'


class StarRate(BaseModel):
    """
    Модель значення зірки рейтингу
    """
    value = models.SmallIntegerField("Значення оцінки рейтингу", default=0)


    def __str__(self):
        return self.value


    class Meta:
        verbose_name = 'Кількість зірок рейтингу'
        verbose_name_plural = 'Кількість зірок рейтингу'


class Rate(models.Model):
    """
    Модель Рейтингу
    """
    ip = models.CharField('Ip-адреса', max_length=25)
    star = models.ForeignKey(StarRate, on_delete=models.CASCADE, verbose_name='Зірка')
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, verbose_name='Фільм')


    def __str__(self):
        return '{star} - {movie}'.format(star=self.star, movie=self.movie)


    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинг'


class Reviews(BaseModel):
    """
    Модель коментарів
    """
    email = models.EmailField()
    name = models.CharField("Ім'я користувача", max_length=25)
    text = models.TextField('Коментарь')
    parent = models.ForeignKey('self', verbose_name='Батьківський коментар', on_delete=models.SET_NULL, null=True, blank=True)
    movie = models.ForeignKey(Movies, verbose_name='Фільм', on_delete=models.CASCADE)


    def __str__(self):
        return '{name} - {movie}'.format(name=self.name, movie=self.movie)


    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'


class Slider(BaseModel):
    """
    Модель слайдера на головній сторінці
    """
    #title = models.CharField('Назва Фільму', max_length=25)
    img = models.ImageField(upload_to='slider/%Y/%m/%d/', max_length=200, unique=True, help_text='Зображення для слайдеру на головній сторінці')
    alt = models.TextField(verbose_name='Підказка', default='')
    index = models.IntegerField(verbose_name='Індекс', default=0)
    movie = models.ForeignKey(Movies, verbose_name='Фільм', on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.name

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайди'