import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("yayınlanma tarihi")

    # Bu fonksiyonlar class'ın İÇİNDE olduğu için 
    # mutlaka 4 boşluk (bir TAB) içeride olmalı!
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        # Soru dün ile bugün arasındaysa TRUE döner
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

