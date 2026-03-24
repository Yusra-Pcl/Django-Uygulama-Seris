from django.urls import path
from . import views

# Bu dosya sadece blog uygulamasına özel yolları tutar
urlpatterns = [
    path('', views.post_list, name='post_list'),
]