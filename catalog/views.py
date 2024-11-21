from django.core.exceptions import PermissionDenied
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product, Category
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from .services import get_products_from_cache
from catalog.services import ProductService


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "product_create.html"
    success_url = reverse_lazy('catalog:home')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorForm
        raise PermissionDenied


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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        category = Category.objects.all()
        context['products_list'] = category

        return context

    def get_queryset(self):
        """ Получаем данные с кэша о продуктах """
        return get_products_from_cache()


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"


class CategoryDetailView(DetailView):
    """ Сортировка товара по категории  """
    model = Category
    template_name = "category.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        category_id = self.object.id
        context["products_list"] = ProductService.get_products_category(category_id)

        return context


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
