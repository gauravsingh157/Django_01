# from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    paginate_by = 5
    context_object_name = 'posts'
    queryset = Post.objects.filter(published=True)

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
