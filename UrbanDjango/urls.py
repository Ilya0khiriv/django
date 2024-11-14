
from django.contrib import admin
from django.urls import path
from task4.views import platform, games, cart, lang
from task5.views import sign_up_by_html, sign_up_by_django



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sign_up_by_html),
    path('django_sign_up/', sign_up_by_django),
    path('platform/', platform),
    path('platform/games', games),
    path('platform/cart', cart),
    path('platform/lang', lang)
]
