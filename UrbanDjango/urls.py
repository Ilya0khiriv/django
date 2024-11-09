
from django.contrib import admin
from django.urls import path
from task2.views import class_view, func_view
from task3.views import platform, games, cart, lang



urlpatterns = [
    path('admin/', admin.site.urls),
    path('cls/', class_view.as_view()),
    path('fnc/', func_view),
    path('platform/', platform),
    path('platform/games', games),
    path('platform/cart', cart),
    path('platform/lang', lang)
]
