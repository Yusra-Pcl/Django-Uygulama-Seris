from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('H', 'Yüksek (Acil)'),
        ('M', 'Orta'),
        ('L', 'Düşük'),
    ]

    title = models.CharField(max_length=200, verbose_name="Görev Başlığı")
    description = models.TextField(blank=True, null=True, verbose_name="Açıklama")
    completed = models.BooleanField(default=False, verbose_name="Tamamlandı mı?")
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M', verbose_name="Öncelik")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['completed', '-created_at']
