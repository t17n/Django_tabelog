from django.urls import path
from .import views
from .views import ShopList, ShopDetail


urlpatterns = [
    path('', views.top, name="top"),
    # path('detail/<int:pk>', ShopDetail.as_view(), name='detail'),
    path('detail/<int:pk>', views.ShopDetail, name='detail'),
    path('search', views.search, name='search'),
    path('genre/<str:genre>', views.genre, name='genre'),
    path('condition/<int:id>', views.condition, name='condition'),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
]

