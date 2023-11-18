from django import forms
from .models import Shop

class SearchForm(forms.Form):
    shop_name = forms.CharField(label='店名', required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    shop_area = forms.CharField(label='駅名', max_length=10, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))

'''
class SearchForm(forms.Form):
    search = forms.CharField(label='店舗検索', required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
'''