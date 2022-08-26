from faker import Factory
import factory 

from common.utils.constants import BLOG_STATUS_CHOICES_FOR_FACTORY, CATEGORIES_CHOICES

from blogs.models import Category, Blog


class CategoryFactory(factory.DjangoModelFactory):
    class Meta:
        model = Category
    name = factory.fuzzy.FuzzyChoice(CATEGORIES_CHOICES) # random choice


class BlogFactory(factory.DjangoModelFactory):
    class Meta:
        model = Blog 
    
    title = factory.Sequence(lambda n: f"Blog post title - {n}")
    category = factory.SubFactory(CategoryFactory) # foreign key -> SubFactory
    excerpt = "This is short description"
    body = factory.Sequence(lambda n: f"This is the blog body - {n}")
    status = factory.fuzzy.FuzzyChoice(BLOG_STATUS_CHOICES_FOR_FACTORY)