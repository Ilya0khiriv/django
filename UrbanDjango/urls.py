
from django.contrib import admin
from django.urls import path
from task4.views import platform, games, cart, lang



urlpatterns = [
    path('admin/', admin.site.urls),
    path('platform/', platform),
    path('platform/games', games),
    path('platform/cart', cart),
    path('platform/lang', lang)
]
