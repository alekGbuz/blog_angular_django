from django.contrib import admin
from site_utils.models import SiteMessages,SiteProfile,SitePage
from solo.admin import SingletonModelAdmin

# Register your models here.


class AdminSiteMessages(admin.ModelAdmin):
    pass

class AdminSiteProfile(SingletonModelAdmin):
    pass


class AdminSitePage(admin.ModelAdmin):
    pass

admin.site.register(SiteMessages, AdminSiteMessages)
admin.site.register(SiteProfile, AdminSiteProfile)
admin.site.register(SitePage, AdminSitePage)