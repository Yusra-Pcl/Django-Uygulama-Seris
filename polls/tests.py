import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Question

# 1. BÖLÜM: Model Testleri (Senin yazdığın kısım)
class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

# 2. BÖLÜM: Sayfa (View) Testleri (Yeni eklediğimiz kısım)
def create_question(question_text, days):
    """Verilen gün farkıyla bir soru oluşturur."""
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """Soru yoksa uygun mesaj görünmeli."""
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Henüz anket mevcut değil.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_future_question(self):
        """Gelecekteki sorular ana sayfada görünmemeli."""
        create_question(question_text="Gelecek Soru.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "Henüz anket mevcut değil.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        """Geçmişteki sorular ana sayfada görünmeli."""
        question = create_question(question_text="Geçmiş Soru.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )