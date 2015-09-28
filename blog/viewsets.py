from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.models import BlogArticle,BlogCategory,BlogSearching
from blog.serializers import BlogArticleSerializer,BlogCategorySerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BlogCategoryViewSet(viewsets.ModelViewSet):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]

class BlogArticleViewSet(viewsets.ModelViewSet):
    queryset = BlogArticle.objects.all()
    serializer_class = BlogArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]

@api_view(['GET'])
def articles_by_category(request, category_slug):
    articles = BlogCategory.objects.get(slug=category_slug).articles.all()
    serialize_articles = BlogArticleSerializer(articles, many=True)
    return Response(serialize_articles.data)

@api_view(['GET'])
def article_by_detail(request,article_slug):
    article = BlogArticle.objects.get(slug=article_slug)
    articles = list(BlogArticle.objects.all())
    index=articles.index(article)
    prev_article_slug=''
    next_article_slug=''
    next_title = ''
    prev_title =''
    if index>0:
        next_article_slug = articles[index-1].slug
        next_title = articles[index-1].title
    if index!=(len(articles)-1):
        prev_article_slug = articles[index+1].slug
        prev_title = articles[index+1].title
    serialize_article = BlogArticleSerializer(article)
    context = {'article':serialize_article.data,'prev_article':{'prev_article_slug':prev_article_slug,'title':prev_title},
               'next_article':{'title':next_title,'next_article_slug':next_article_slug}}
    return Response(context)

@api_view(['GET'])
def articles_by_keys(request):
    keys = request.query_params.get('keys')

    search = BlogSearching.objects.create(search=keys)

    keys = keys.lower().split()
    articles = BlogArticle.objects.all()
    articles_by_keys = []
    for article in articles:
        for key in keys:
            if key in article.title.lower() or key in article.content.lower():
                articles_by_keys.append(article)
                break
    serialize_articles_by_keys = BlogArticleSerializer(articles_by_keys, many=True)
    return Response(serialize_articles_by_keys.data)




