# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields
import autoslug.fields
import blog.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteMessages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254, verbose_name='\u041f\u043e\u0447\u0442\u0430')),
                ('title', models.CharField(max_length=500, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('content', models.TextField(verbose_name='\u0421\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435')),
                ('message_file', models.FileField(upload_to=b'message_file', verbose_name='\u0424\u0430\u0439\u043b', blank=True)),
                ('date', models.DateField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430')),
            ],
            options={
                'ordering': ['pk'],
                'verbose_name': '\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f',
            },
        ),
        migrations.CreateModel(
            name='SitePage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b')),
                ('content', redactor.fields.RedactorField(verbose_name='\u0421\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=b'name', unique=True, slugify=blog.models.custom_slugify)),
            ],
            options={
                'verbose_name': '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 \u0441\u0430\u0439\u0442\u0430',
                'verbose_name_plural': '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u044b \u0441\u0430\u0439\u0442\u0430',
            },
        ),
        migrations.CreateModel(
            name='SiteProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meta_keywords', models.TextField(verbose_name='\u041a\u043b\u044e\u0447\u0435\u0432\u044b\u0435 \u0441\u043b\u043e\u0432\u0430')),
                ('meta_description', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('copy_sign', models.CharField(max_length=200, verbose_name='\u0417\u0430\u0449\u0438\u0442\u0430 \u043f\u0440\u0430\u0432')),
            ],
            options={
                'verbose_name': '\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0441\u0430\u0439\u0442\u0430',
            },
        ),
    ]
