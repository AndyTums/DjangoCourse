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

        return HttpResponse(f"Спасибо! На ваш mail {mail} отправлена сообщение о регистрации вашего обращения!")
    return render(request, "contacts.html")
