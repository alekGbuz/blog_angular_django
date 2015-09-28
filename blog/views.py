from django.shortcuts import render_to_response
from blog.models import  BlogCategory,BlogArticle
from site_utils.models import SiteProfile,SitePage

# Create your views here.

def index_page(request):
    categories = BlogCategory.objects.all()
    count = categories.count()/2
    categories_left = categories[0:count]
    categories_right = categories[count:]
    site_profile = SiteProfile.get_solo()
    pages = SitePage.objects.all()

    articles = BlogArticle.objects.all()[:5]
    context = {'articles':articles, 'categories_left':categories_left,'categories_right':categories_right,'site_profile':site_profile,'pages':pages}
    return render_to_response('base.html',context)
