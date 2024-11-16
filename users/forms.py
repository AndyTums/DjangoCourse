from django import forms
from django.contrib.auth.forms import UserCreationForm

from catalog.forms import StyleFormMixin
from users.models import User


class CustomCreationForm(StyleFormMixin, UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('email', 'password1')

    # def clean_phone_number(self):
    #     phone = self.cleaned_data.get('phone')
    #     if phone and phone.isdigit():
    #         raise forms.ValidationError("Номер должен состоять только из цифр")
    #     return phone
