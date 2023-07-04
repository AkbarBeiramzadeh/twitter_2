from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # اگر یک یوزر حذف شد پست هایش نیز حذف می شود.
    title = models.CharField(max_length=240)
    body = models.TextField()
    slug = models.SlugField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
