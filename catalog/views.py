from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Product, Category
from django.views.generic import ListView, UpdateView, DetailView, DeleteView


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


class ContactView(ListView):
    model = Product
    template_name = "contacts.html"


def user_contact(request):
    if request.method == "POST":
        mail = request.POST.get("name")
        message = request.POST.get("message")

        return render(request, "user_contact.html")
        # return HttpResponse(f"Заявка отправлена на почту!")
    return render(request, "contacts.html")
