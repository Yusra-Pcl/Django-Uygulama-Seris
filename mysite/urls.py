from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),          # Yönetim paneli kapısı
    path('polls/', include('polls.urls')),   # 1. Uygulama (Anket) kapısı
    path('blog/', include('blog.urls')),     # 2. Uygulama (Blog) kapısı -> YENİ EKLEDİK!
]
