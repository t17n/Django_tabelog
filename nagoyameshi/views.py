from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Shop
from django.views.generic import ListView, DetailView
from .forms import SearchForm

# Create your views here.
'''
def hello_world(request, name):
    return HttpResponse(f"Hello{name}")
'''

def top(request):
    form = SearchForm()
    params = {
        'form': form,
    }
    return render(request, 'nagoyameshi/top.html', params)


def search(request):
    form = SearchForm()
    data = Shop.objects.all()
    # search_keyword = None
    
    if (request.method == 'POST'):
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']
            data = Shop.objects.filter(name__contains=search)

    params = {
        'form': form,
        'data': data,
        # 'search_keyword': search_keyword,
    }
    return render(request, 'nagoyameshi/search.html', params)


class ShopList(ListView):
    model = Shop

class ShopDetail(DetailView):
    model = Shop

