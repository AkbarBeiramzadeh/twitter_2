from django.shortcuts import render
from django.views import View
from .models import Post


class HomeView(View):
    def get(self, request):
        posts = Post.objects.all()
        context = {
            'posts': posts
        }
        return render(request, template_name='home/index.html', context=context)


class PostDetailView(View):
    def get(self, request, post_id, post_slug):
        post = Post.objects.get(pk=post_id, slug=post_slug)
        return render(request, 'home/detail.html', {'post': post})
