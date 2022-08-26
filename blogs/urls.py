from django.urls import path

from .views import ListBlogView

app_name='blog'

urlpatterns = [
    path('blogs/', ListBlogView.as_view()),
]