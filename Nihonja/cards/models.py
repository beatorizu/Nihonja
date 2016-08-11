from django.db import models

class Card(models.Model):

    phrase = models.CharField('Frase', max_length=100)
    slug = models.SlugField('Atalho')
    kanji = models.CharField('Kanji')
    image = models.ImageField(upload_to='cards/images', verbose_name='Image')

    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)
