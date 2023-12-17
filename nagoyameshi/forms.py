from django import forms
from .models import Shop

class SearchForm(forms.Form):
    shop_name = forms.CharField(label='店名', required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    shop_area = forms.CharField(label='駅名', max_length=10, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))

'''
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit
from .models import Shop

class SearchForm(forms.Form):
    shop_name = forms.CharField(label='店名', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    shop_area = forms.CharField(label='駅名', max_length=10, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Div('shop_name', css_class='mb-3'),
                Div('shop_area', css_class='mb-3'),
                css_class='row'
            ),
            Div(
                Div(Submit('submit', '検索', css_class='btn btn-secondary btn-sm'), css_class='col-md-9 offset-md-3'),
                css_class='row'
            ),
        )
'''

'''
class SearchForm(forms.Form):
    search = forms.CharField(label='店舗検索', required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
'''