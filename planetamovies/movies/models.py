from django.db import models

# Create your models here.
class Category(models.Model):
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