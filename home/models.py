from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='posts')  # اگر یک یوزر حذف شد پست هایش نیز حذف می شود.
    title = models.CharField(max_length=240)
    body = models.TextField()
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']  # مرتب سازی پست ها بر اساس تاریخ

    def get_absolute_url(self):
        return reverse('home:post_detail', args=(self.id, self.slug))

    def __str__(self):
        return f"{self.user} / {self.title}"
