from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import SignupView

# NoReverseMatchエラー 対応
from .views import SignupView, CustomLoginView, CustomLogoutView

app_name = "accounts"

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
]

