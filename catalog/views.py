from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home_page.html')


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
