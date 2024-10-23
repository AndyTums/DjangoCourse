from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Product, Category


def home(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "home_page.html", context)


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {"product": product}
    return render(request, "product_detail.html", context)


def category(request):
    return render(request, 'category.html')


def order(request):
    return render(request, 'catalog.html')


def contact(request):
    return render(request, 'contacts.html')


def user_contact(request):
    if request.method == "POST":
        mail = request.POST.get("name")
        message = request.POST.get("message")

        return render(request, "user_contact.html")
        # return HttpResponse(f"Заявка отправлена на почту!")
    return render(request, "contacts.html")
