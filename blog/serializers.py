from blog.models import BlogArticle,BlogCategory
from rest_framework import serializers

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory

class BlogArticleSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer(many=True)
    class Meta:
        model = BlogArticle
