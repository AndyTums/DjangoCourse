from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from blog.models import Blogs
from django.views.generic import ListView, UpdateView, DetailView, DeleteView, CreateView


class BlogListView(ListView):
    model = Blogs
    template_name = 'blog_list.html'

    def get_queryset(self):
        return Blogs.objects.filter(is_published=True)


class BlogDetailView(DetailView):
    model = Blogs
    template_name = 'blog_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blogs
    template_name = "blog_create.html"
    fields = ["title", "text", "created_at", "is_published", "image"]
    success_url = reverse_lazy("blog:blog_list")


class BlogUpdateView(UpdateView):
    model = Blogs
    template_name = "blog_create.html"
    fields = ["title", "text", "created_at", "is_published", "image"]
    success_url = reverse_lazy("blog:blog_list")

    def get_success_url(self):
        return reverse("blog:blog_detail", args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blogs
    template_name = "blog_confirm_delete.html"
    success_url = reverse_lazy("blog:blog_list")
