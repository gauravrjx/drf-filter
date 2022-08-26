from django.db import models

from common.models.abstract_base import BaseModel
from common.utils.constants import (
    BLOG_STATUS_CHOICES, DRAFT, PUBLISHED)



class Category(BaseModel):
    """
    Categories for Blog posts such as `Politics`, `Information Technology`
    """
    name = models.CharField(
        max_length=25, db_index=True, unique=True)
    name_ne = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-modified_at"]



class Blog(BaseModel):
    """
    Blog posts, CRUD by anyone 
    """

    title = models.CharField(
        max_length=255, db_index=True, unique=True)
    category = models.ForeignKey(
        Category, related_name='blogs',
        on_delete=models.CASCADE)
    excerpt = models.TextField(blank=True)
    body = models.TextField()
    status = models.CharField(
        choices=BLOG_STATUS_CHOICES, default=DRAFT, max_length=50,
        db_index=True)

    class Meta:
        ordering = ("-created_at", )

    def __str__(self):
        return f"{self.title} "
