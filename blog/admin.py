from django.contrib import admin
from blog.models import BlogCategory,BlogArticle,BlogSearching
# Register your models here.


class AdminBlogSearching(admin.ModelAdmin):
    list_display = ('date','search')

    class Meta:
        model = BlogSearching

class AdminBlogArticle(admin.ModelAdmin):
    exclude = ['description']

    class Meta:
        model = BlogArticle

class AdminBlogCategory(admin.ModelAdmin):
    pass

admin.site.register(BlogCategory,AdminBlogCategory)
admin.site.register(BlogArticle,AdminBlogArticle)
admin.site.register(BlogSearching,AdminBlogSearching)
