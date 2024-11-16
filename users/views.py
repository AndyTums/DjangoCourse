from django.contrib.auth import logout
from django.core.mail import send_mail
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from .forms import CustomCreationForm
from .models import User
import secrets
from config.settings import EMAIL_HOST_USER


class RegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = CustomCreationForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(subject="Потверждение почты", message=f"Рады вашей регистрации!Осталось потвердить почту!{url}",
                  from_email=EMAIL_HOST_USER, recipient_list=[user.email])

        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


def user_logout(request):
    logout(request)
    return render(request, template_name="home_page.html")
