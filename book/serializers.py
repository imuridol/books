from rest_framework import serializers
from .models import *

class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = '__all__'

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'

class BookModelSerializer(serializers.ModelSerializer):
    author = AuthorModelSerializer()
    category = CategoryModelSerializer()

    class Meta:
        model = BookModel
        fields = "__all__"