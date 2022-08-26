from django.utils import timezone
from rest_framework import serializers

from .helpers import get_today, combine_date_parts


def is_future_datetime(year: int = 0, month: int = 0, day: int = 1):
    """
    compares provided_date with today's date and raises validation error
    if provided_date is less than today's date
    """

    provided_date = combine_date_parts(year, month, day)

    if not provided_date:
        raise serializers.ValidationError(_(
            'Invalid Date Passed.'
        ))

    if provided_date < get_today():
        raise serializers.ValidationError(_(
            'Date Must be in future.'
        ))
