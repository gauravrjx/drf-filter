# from dataclasses import fields
from rest_framework import serializers

from .models import Category, Blog


class CategorySeriaizer(serializers.ModelSerializer):

    # change default datetime format `2022-08-26T08:11:47.300638Z` to
    # `2022-08-26, 11:47 AM`
    created_at = serializers.DateTimeField(format="%Y-%m-%d, %I:%M:%S %p")
    modified_at = serializers.DateTimeField(format="%Y-%m-%d, %I:%M:%S %p")

    class Meta:
        model= Category 
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    category = CategorySeriaizer()  # FK

    created_at = serializers.DateTimeField(format="%Y-%m-%d, %I:%M:%S %p")
    modified_at = serializers.DateTimeField(format="%Y-%m-%d, %I:%M:%S %p")


    class Meta:
        model= Blog
        fields = '__all__'
