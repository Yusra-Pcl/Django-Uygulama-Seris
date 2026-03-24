from django.contrib import admin
from .models import Post

# Hocanın admin panelinde blog yazılarını şık bir şekilde görmesi için:
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date') # Listede görünecek sütunlar
    list_filter = ('published_date', 'author')           # Sağ taraftaki filtreleme
    search_fields = ('title', 'text')                   # Arama kutusu
    date_hierarchy = 'published_date'                    # Takvim hiyerarşisi

