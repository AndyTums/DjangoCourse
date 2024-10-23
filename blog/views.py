from django.shortcuts import render
from blog.models import Blogs
from django.views.generic import ListView, UpdateView, DetailView, DeleteView


class BlogListView(ListView):
    model = Blogs
    template_name = 'blog_list.html'

# Create your views here.
