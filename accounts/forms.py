from django.contrib.auth.forms import UserCreationForm
from nagoyameshi.models import Member


class SignupForm(UserCreationForm):
    class Meta:
        model = Member
        fields = ('username', 'email', 'cardholder_name', 'card_number', 'expiration_date', 'cvv')