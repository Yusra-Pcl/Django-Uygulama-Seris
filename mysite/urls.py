from django.contrib import admin
from django.urls import include, path  # 'include' kelimesinin burada olması ŞART!

urlpatterns = [
    path('admin/', admin.site.urls),           # Yönetim paneli yolu
    path('polls/', include('polls.urls')),    # Anket uygulaması yolu
    path('blog/', include('blog.urls')),      # Blog uygulaması yolu
    path('todo/', include('todo.urls')),      # İŞTE BU SATIR: Todo uygulamasının kapısını açar
]