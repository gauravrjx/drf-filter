from django.db import models

# Create your models here.
class BaseModel(models.Model):
    """Base model for this project."""
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

