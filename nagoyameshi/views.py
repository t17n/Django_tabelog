from django.shortcuts import render, redirect
from .models import Shop
from django.views.generic import ListView, DetailView
from .forms import SearchForm
from django.db.models import Q


def top(request):
    form = SearchForm()
    genres = Shop.GENRE_CHOICES
    params = {
        'form': form,
        'genres': genres,
    }
    return render(request, 'nagoyameshi/top.html', params)

def search(request):
    if (request.method == 'POST'):
        form = SearchForm(request.POST)
        if form.is_valid():
            shop_name = form.cleaned_data['shop_name']
            shop_area = form.cleaned_data['shop_area']

            # ChatGPT先生
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

    params = {
        'form': form,
        'data': data,
    }
    return render(request, 'nagoyameshi/search.html', params)

def genre(request, genre):
    # genre = request.GET.get('genre', '')
    data = Shop.objects.filter(genre=genre)

    params = {
        'data': data
    }
    return render(request, 'nagoyameshi/search.html', params)


'''
#店名、エリア・駅名 
def search(request):
    if (request.method == 'POST'):
        form = SearchForm(request.POST)
        if form.is_valid():
            shop_name = request.POST['shop_name']
            shop_aria = request.POST['shop_aria']
            data = Shop.objects.filter\
                (Q(name__contains=shop_name) | Q(neareststation__contains=shop_aria))
    params = {
        'form': form,
        'data': data,
    }
    return render(request, 'nagoyameshi/search.html', params)
'''

'''
# 店名のみ
def search(request):
    # form = SearchForm()
    # data = Shop.objects.all()
    # search_keyword = None
    
    if (request.method == 'POST'):
        form = SearchForm(request.POST)
        if form.is_valid():
            search = request.POST['search']
            # search = form.cleaned_data['search']
            data = Shop.objects.filter(name__contains=search)

    params = {
        'form': form,
        'data': data,
        # 'search_keyword': search_keyword,
    }
    return render(request, 'nagoyameshi/search.html', params)
'''

class ShopList(ListView):
    model = Shop

class ShopDetail(DetailView):
    model = Shop