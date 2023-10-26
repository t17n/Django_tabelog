from django.urls import path
from . import views

urlpatterns = [
    path('hello/<str:name>', views.hello_world, name="hello_world"),
]