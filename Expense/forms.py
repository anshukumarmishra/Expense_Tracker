from django import forms
from .models import Expense , User

class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense

        exclude = ["user"]

class UserForm(forms.ModelForm):

    confirm_password = forms.CharField(
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["username", "email", "password"]

        widgets = {
            "password": forms.PasswordInput()
        }


from django import forms

class LoginForm(forms.Form):

    username = forms.CharField(
        max_length=100
    )

    password = forms.CharField(
        widget=forms.PasswordInput()
    )