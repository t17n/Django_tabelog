from django.shortcuts import render, redirect, get_object_or_404
from .models import Shop, Condition, Genre
from django.views.generic import ListView, DetailView
from .forms import SearchForm
from django.db.models import Q
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator


def top(request):
    form = SearchForm()
    genres = Genre.objects.all()
    conditions = Condition.objects.all()
    params = {
        'form': form,
        'genres': genres,
        'conditions': conditions,
    }
    return render(request, 'nagoyameshi/top.html', params)

# キーワード検索
def search(request):
    if (request.method == 'POST'):
        form = SearchForm(request.POST)
        if form.is_valid():
            shop_name = form.cleaned_data['shop_name']
            shop_area = form.cleaned_data['shop_area']

            # 両方が空でない場合はAND条件で検索
            if shop_name and shop_area:
                data = Shop.objects.filter(Q(name__contains=shop_name) & Q(neareststation__contains=shop_area))

            # どちらかが空の場合はそれぞれの条件に該当するデータを取得
            else:
                query = Q()
                if shop_name:
                    query |= Q(name__contains=shop_name)
                if shop_area:
                    query |= Q(neareststation__contains=shop_area)
                data = Shop.objects.filter(query)
    page = Paginator(data, 9)
    params = {
        'form': form,
        'data': page.get_page(id),
    }
    return render(request, 'nagoyameshi/search.html', params)

# ジャンル検索
# 値で検索するパターン
# def genre(request, genre):
    # data = Shop.objects.filter(genre=genre)
# idで検索するパターン
def genre(request, id):
    data = Shop.objects.filter(genre__id=id)
    page = Paginator(data, 9)
    params = {
        'data': page.get_page(id),
    }
    return render(request, 'nagoyameshi/search.html', params)

# こだわり条件検索
def condition(request, id):
    data = Shop.objects.filter(condition__id=id)
    page = Paginator(data, 9)
    params = {
        'data': page.get_page(id),
    }
    return render(request, 'nagoyameshi/search.html', params)


class ShopList(ListView):
    model = Shop

def ShopDetail(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    conditions = shop.condition.all()
    params = {
        'shop': shop,
        'conditions': conditions,
    }
    return render(request, "nagoyameshi/shop_detail.html", params)
'''
class LoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'nagoyameshi/login.html'

class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'top.html'
'''

