# from email.quoprimime import body_check
from common.utils.constants import (
    CATEGORIES_CHOICES, 
    BLOG_STATUS_CHOICES,
    PENDING,
    PUBLISHED,
    DRAFT,
    DENIED
)
from django.db.models import Q
import django_filters.rest_framework as filters
from .models import Category, Blog



class BlogFilter(filters.FilterSet):
    """
    creating custom filtering 
    - so that `fields` seems beautiful
    """
    # status_choices = list(CATEGORIES_CHOICES)
    blog_status_choices = list(BLOG_STATUS_CHOICES)

    category = filters.CharFilter(
        field_name='category__name ', # override name `category__name` to `category`
        label='category name', # `label` will be shown in browsable API form
        # lookup_expr='in', # default `exact`
        method='filter_by_category'
    )

    status = filters.ChoiceFilter(
        choices=blog_status_choices,
        method='filter_by_status',
    )

    @staticmethod
    def filter_by_category(queryset, field, value):
        if 'any' in value:
            return queryset
        else:
            queryset = queryset.filter(
                category__name=value
            )
        return queryset

    @staticmethod 
    def filter_by_status(queryset, field, value):
        choice_query_filter = {
            'Pending': Q(status=PENDING),
            'Published': Q(status=PUBLISHED),
            'Denied': Q(status=DENIED),
        }

        return queryset.filter(choice_query_filter.get(value, Q()))
    

    class Meta:
        model = Blog
        fields = ['category', 'status',] 
        