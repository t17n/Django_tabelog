from django.urls import path
from . import views
from .views import ShopList, ShopDetail

urlpatterns = [
    # path('hello/<str:name>', views.hello_world, name="hello_world"),
    path('', views.top, name="top"),
    path('detail/<int:pk>', ShopDetail.as_view(), name='detail'),
    path('search', views.search, name='search'),
]