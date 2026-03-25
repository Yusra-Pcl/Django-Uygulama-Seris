from django.contrib import admin
from django.urls import include, path  # 'include' kelimesinin burada olması ŞART!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('weather/', include('weather.urls')),
    path('polls/', include('polls.urls')),
    path('blog/', include('blog.urls')),
    path('todo/', include('todo.urls')),
    # BURADA WEATHER SATIRI EKSİK OLABİLİR!
]