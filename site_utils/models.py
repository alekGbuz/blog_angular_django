 # -*- coding: utf-8 -*-
from django.db import models
from solo.models import SingletonModel
from autoslug import AutoSlugField
from blog.models import custom_slugify
from redactor.fields import RedactorField

class SitePage(models.Model):
    name = models.CharField(u'Название страницы',max_length=500)
    content = RedactorField(u'Содержание')
    slug = AutoSlugField(populate_from='name', unique=True, slugify=custom_slugify)


    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name=u'Страница сайта'
        verbose_name_plural=u'Страницы сайта'



class SiteProfile(SingletonModel):
    meta_keywords = models.TextField(u'Ключевые слова')
    meta_description = models.TextField(u'Описание')
    copy_sign = models.CharField(u'Защита прав',max_length=200)

    class Meta:
        verbose_name = u'Настройки сайта'


class SiteMessages(models.Model):
    email = models.EmailField(u'Почта')
    title = models.CharField(u'Заголовок',max_length=500)
    content = models.TextField(u'Содержание')
    message_file = models.FileField(u'Файл',upload_to='message_file', blank=True)
    date = models.DateField(u'Дата',auto_now=True)

    class Meta:
        ordering = ['pk']
        verbose_name = u'Сообщение'
        verbose_name_plural = u'Сообщения'

    def __unicode__(self):
        return self.title


