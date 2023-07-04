from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'slug', 'updated')
    search_fields = ('title',)
    list_filter = ('updated',)
    prepopulated_fields = {'slug': ('body',)} # این نوع پر کردن slug فقط در ادمین پنل می باشد.
    raw_id_fields = ('user',)
