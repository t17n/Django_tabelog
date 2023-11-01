from django.urls import path
from . import views

urlpatterns = [
    # path('hello/<str:name>', views.hello_world, name="hello_world"),
    path('', views.top, name='top'),
    # path('search/', views.search, name='search'),
    # path('login/', views.login, name='login'),
    # path('register/', views.register, name='register'),
]