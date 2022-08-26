from email.quoprimime import body_check
from common.utils.constants import CATEGORIES_CHOICES
import django_filters.rest_framework as filters

from .models import Category, Blog


class BlogFilter(filters.FilterSet):
    status_choices = list(CATEGORIES_CHOICES)

    title = filters.CharFilter(
        label='Blog Title',
        lookup_expr='exact'
    )
    category = filter.ModelChoiceFields(
        label='Category',
        field_name='Category__name',
        lookup_expr='in',
        method='filter_by_category'
    )
    excerpt = filter.CharFilter(
        label='excerpt',
        lookup_expr='exact'
    )
    body = filter.CharFilter(
        label='Blog body'
    )
    status = filter.ChoiceFilter(
        label='Blog Status'
        choices=status_choices,
        method='filter_review_status'
    )
    #TODO: body, status, 

    @staticmethod
    def filter_by_category(queryset, field, value):
        if 'any' in value:
            return queryset
        else:
            queryset = queryset.filter(
                categories__name__in=value
            )
        return queryset