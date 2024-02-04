from django.urls import path
from .import views

app_name = 'nagoyameshi'

urlpatterns = [
    path('', views.top, name="top"),
    path('detail/<int:pk>', views.ShopDetail, name='detail'),
    path('detail/<int:pk>', views.CreateReview.as_view(), name='detail'),
    path('search', views.search, name='search'),
    path('genre/<int:id>', views.genre, name='genre'),
    path('condition/<int:id>', views.condition, name='condition'),
    # path('login/', views.LoginView.as_view(), name="login"),
    # path('logout/', views.LogoutView.as_view(), name="logout"),
]