from django import forms
from .models import Shop

'''
モデル作成用フォーム
class ShopSeachForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['name']
        name = forms.CharField(label='name')
'''

class SearchForm(forms.Form):
    search = forms.CharField(label='店舗検索', required=False, widget=forms.TextInput(attrs={'class':'form-control'}))