# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import blog.models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('description', models.CharField(max_length=500, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=b'title', unique=True, slugify=blog.models.custom_slugify)),
                ('date', models.DateField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430')),
                ('content', redactor.fields.RedactorField(verbose_name='\u0421\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435')),
            ],
            options={
                'ordering': ['pk'],
                'verbose_name': '\u041f\u043e\u0441\u0442',
                'verbose_name_plural': '\u041f\u043e\u0441\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=b'title', unique=True, slugify=blog.models.custom_slugify)),
            ],
            options={
                'ordering': ['-pk'],
                'verbose_name': '\u0422\u0435\u0433',
                'verbose_name_plural': '\u0422\u0435\u0433\u0438',
            },
        ),
        migrations.CreateModel(
            name='BlogSearching',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('search', models.CharField(max_length=500)),
                ('date', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['pk'],
                'verbose_name': '\u041f\u043e\u0438\u0441\u043a\u043e\u0432\u044b\u0439 \u0437\u0430\u043f\u0440\u043e\u0441',
                'verbose_name_plural': '\u041f\u043e\u0438\u0441\u043a\u043e\u0432\u044b\u0435 \u0437\u0430\u043f\u0440\u043e\u0441\u044b',
            },
        ),
        migrations.AddField(
            model_name='blogarticle',
            name='category',
            field=models.ManyToManyField(related_name='articles', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438', to='blog.BlogCategory'),
        ),
    ]
