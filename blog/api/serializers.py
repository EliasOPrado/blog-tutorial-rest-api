from rest_framework import serializers
from blog.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    """ serializer for Article model """
    class Meta:
        model = Article
        fields = ['id','title','body','date','thumb']
