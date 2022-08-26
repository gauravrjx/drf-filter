import os
import uuid
import datetime

from django.utils import timezone


def get_today():
    return timezone.now().astimezone().date()


def combine_date_parts(year: int = 0, month: int = 0, day: int = 1):
    """
    Combines date parts and returns date
    :param year: Year int
    :param month: Month int
    :param day: Day int (defaults to 1)
    :return: datetime.date instance if valid and None if invalid
    """
    date_kwargs = {'day': day}

    if year:
        date_kwargs['year'] = year
    if month:
        date_kwargs['month'] = month

    try:
        return datetime.date(**date_kwargs)
    except (OverflowError, ValueError, TypeError):
        return None
