from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomCreationForm
from .models import User


class RegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = CustomCreationForm
    success_url = reverse_lazy('catalog:home')
