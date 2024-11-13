from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from catalog.forms import ProductForm
from catalog.models import Product, Category
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "product_create.html"
    success_url = reverse_lazy('catalog:home')


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product_create.html"
    success_url = reverse_lazy('catalog:home')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "product_confirm_delete.html"
    success_url = reverse_lazy('catalog:home')


class ProductListView(ListView):
    model = Product
    template_name = "home_page.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"


class CategoryListView(ListView):
    model = Category
    template_name = "category.html"


class OrderListView(ListView):
    model = Product
    template_name = "catalog.html"


class ContactView(TemplateView):
    model = Product
    template_name = "contacts.html"


def user_contact(request):
    if request.method == "POST":
        mail = request.POST.get("name")
        message = request.POST.get("message")

        return render(request, "user_contact.html")
        # return HttpResponse(f"Заявка отправлена на почту!")
    return render(request, "contacts.html")
