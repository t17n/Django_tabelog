from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nagoyameshi/', include('nagoyameshi.urls')),
    path('accounts/', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    # path('hello/<str:name>', views.hello_world, name="hello_world"),
    # path('nagoyameshi/', include('nagoyameshi.urls')), 
    # path('search/', include('nagoyameshi.urls', 'search')),
    # path('login/', include('nagoyameshi.urls', 'login')),
    # path('register/', include('nagoyameshi.urls', 'register')),