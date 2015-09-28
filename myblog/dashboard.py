 # -*- coding: utf-8 -*-
"""
This file was generated with the customdashboard management command, it
contains the two classes for the main dashboard and app index dashboard.
You can customize these classes as you want.

To activate your index dashboard add the following to your settings.py::
    ADMIN_TOOLS_INDEX_DASHBOARD = 'myblog.dashboard.CustomIndexDashboard'

And to activate the app index dashboard::
    ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'myblog.dashboard.CustomAppIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from admin_tools.dashboard import modules, Dashboard, AppIndexDashboard
from admin_tools.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for myblog.
    """
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        # append a link list module for "quick links"
        self.children.append(modules.LinkList(
            _(U'Ссылки'),
            layout='inline',
            draggable=False,
            deletable=False,
            collapsible=False,
            children=[
                [_(u'На сайт'), '/'],
                [_(u'Смена пароля'),
                 reverse('%s:password_change' % site_name)],
                [_(u'Выйти'), reverse('%s:logout' % site_name)],
            ]
        ))

        # append an app list module for "Applications"
        # self.children.append(modules.AppList(
        #     _('Applications'),
        #     exclude=('django.contrib.*',),
        # ))

        self.children.append(modules.ModelList(
            _(u'Инструменты сайта'),
            models=(
                'site_utils.models.SiteProfile',
                'site_utils.models.SiteMessages',
                'site_utils.models.SitePage',
            ),

        ))
        self.children.append(modules.ModelList(
               _(u'Блог'),
              models=(
                'blog.models.BlogArticle',
                'blog.models.BlogCategory',
                'blog.models.BlogSearching',
              ),
        ))

        # append an app list module for "Administration"
        # self.children.append(modules.AppList(
        #     _('Administration'),
        #     models=('django.contrib.*',),
        # ))

        # append a recent actions module
        self.children.append(modules.RecentActions(_(u'Последние события'), 5))

        # append a feed module
        # self.children.append(modules.Feed(
        #     _('Latest Django News'),
        #     feed_url='http://www.djangoproject.com/rss/weblog/',
        #     limit=5
        # ))

        # append another link list module for "support".
        # self.children.append(modules.LinkList(
        #     _('Support'),
        #     children=[
        #         {
        #             'title': _('Django documentation'),
        #             'url': 'http://docs.djangoproject.com/',
        #             'external': True,
        #         },
        #         {
        #             'title': _('Django "django-users" mailing list'),
        #             'url': 'http://groups.google.com/group/django-users',
        #             'external': True,
        #         },
        #         {
        #             'title': _('Django irc channel'),
        #             'url': 'irc://irc.freenode.net/django',
        #             'external': True,
        #         },
        #     ]
        # ))


class CustomAppIndexDashboard(AppIndexDashboard):
    """
    Custom app index dashboard for myblog.
    """

    # we disable title because its redundant with the model list module
    title = ''

    def __init__(self, *args, **kwargs):
        AppIndexDashboard.__init__(self, *args, **kwargs)

        # append a model list module and a recent actions module
        if self.app_title==u'Блог':
            self.children += [
                modules.ModelList(self.app_title, ['blog.models.BlogCategory','blog.models.BlogArticle',
                                                   'blog.models.BlogSearching']),
                ]
        if self.app_title == u'Настройки сайта':
            self.children += [
                modules.ModelList(self.app_title, ['site_utils.models.SiteProfile','site_utils.models.SiteMessages',
                                                   'site_utils.models.SitePage']),
            ]

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        return super(CustomAppIndexDashboard, self).init_with_context(context)
