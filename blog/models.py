from django.db import models
from django.utils.text import slugify
from googletrans import Translator


class PostSite(models.Model):
    title = models.CharField(max_length=20, verbose_name='Заголовок')
    text = models.CharField(max_length=40, verbose_name='Описание')
    date = models.DateField(auto_now=True, verbose_name='Время создание')
    date_db = models.DateTimeField(auto_now_add=True, verbose_name='Время создание')
    slug = models.SlugField(max_length=20, unique=True,
                            blank=True, verbose_name='Slug')

    class Meta:
        verbose_name = 'Посты сайта'
        verbose_name_plural = 'Посты сайта'
        ordering = ['-date_db']

    def save(self, *args, **kwargs):
        if not self.slug:
            translator = Translator()
            translation = translator.translate(self.title, dest='en')
            self.slug = slugify(translation.text)
            unique_slug = self.slug
            num = 1
            while PostSite.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{self.slug}-{num}'
                num += 1
            self.slug = unique_slug

        super(PostSite, self).save(*args, **kwargs)
