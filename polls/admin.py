from django.contrib import admin
from .models import Question, Choice

# Soruları ve Seçenekleri yan yana ekleyebilmek için şık bir görünüm:
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3 # Varsayılan olarak 3 seçenek kutusu açar

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Tarih Bilgisi", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)
admin.site.site_header = "Tuna Proje Yönetim Paneli"
admin.site.site_title = "Tuna Admin"
admin.site.index_title = "Anket Uygulaması Kontrol Merkezi"