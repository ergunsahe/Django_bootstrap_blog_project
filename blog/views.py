from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class BlogPageView(ListView):
    model = Post
    template_name = "index.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "post.html"