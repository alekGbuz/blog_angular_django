 # -*- coding: utf-8 -*-
from django.db import models
from redactor.fields import RedactorField
from autoslug import AutoSlugField
# Create your models here.
from autoslug.settings import slugify as default_slugify


def custom_slugify(value):
    return  ''.join([ i for i in default_slugify(value).replace(' ','_') if i.isalpha() or i=='_'])


class BlogCategory(models.Model):
    title = models.CharField(u'Название',max_length=500)
    slug = AutoSlugField(populate_from='title',unique=True, slugify=custom_slugify)

    def __unicode__(self):
        return self.title


    class Meta:
        verbose_name = u'Тег'
        verbose_name_plural = u'Теги'
        ordering=['-pk']


class BlogArticle(models.Model):
    title = models.CharField(u'Название',max_length=500)
    description = models.CharField(u'Описание',max_length =500)
    slug = AutoSlugField(populate_from='title', unique=True,slugify=custom_slugify)
    category = models.ManyToManyField(BlogCategory, verbose_name=u'Категории', related_name='articles')
    date = models.DateField(u'Дата',auto_now=True)
    content = RedactorField(u'Содержание')

    def __unicode__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.description = self.content[:300]+'[...]'
        super(BlogArticle,self).save(*args,**kwargs)


    class Meta:
        ordering = ['-pk']
        verbose_name = u'Пост'
        verbose_name_plural = u'Посты'




class BlogSearching(models.Model):
    search = models.CharField(max_length=500)
    date = models.DateField(auto_now=True)

    class Meta:
        ordering =['pk']
        verbose_name = u'Поисковый запрос'
        verbose_name_plural = u'Поисковые запросы'
