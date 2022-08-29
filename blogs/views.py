from django.shortcuts import render

from rest_framework import generics
from blogs.filter_classes import BlogFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Category, Blog
from .serializers import CategorySeriaizer, BlogSerializer
# Create your views here.


# class ListBlogView(generics.ListAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#     filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
#     search_fields = ['title', 'category__name',]
#     filterset_fields = [
#         'status',
#         'category__name'
#     ]
#     ordering_fields = [
#         'title',
#         'created_at',
#         'modified_at',
#     ]


class ListBlogView(generics.ListAPIView):
    """
    The above `ListBlogView` works just fine, but when it comes to `search/filter`,
    double underscores are to be used `category__name` which looks ugly. 
    We can create own `FiterSet` classes.
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filterset_class = BlogFilter
    search_fields = ['title',]
    ordering_fields = [
        'created_at',
        'modified_at',
    ]
