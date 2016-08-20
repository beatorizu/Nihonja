from audiofield.fields import AudioField
from django.db import models

class CardManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(phrase__icontains=query) |
            models.Q(kanji__icontains=query)
        )

class Card(models.Model):

    phrase = models.CharField('Frase', max_length=100)
    slug = models.SlugField('Atalho')
    kanji = models.TextField('Kanji')
    audio = AudioField(upload_to='cards/audios',
                        ext_whitelist=('.mp3', '.wav', '.ogg'),
                        help_text=('Allowed type - .mp3, .wav, .ogg'), null=True, blank=True)

    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)

    objects = CardManager()

    def __str__(self):
        return self.phrase

    class Meta:
        verbose_name = 'Cartão'
        verbose_name_plural = 'Cartões'
        ordering = ['phrase']
