from django.test import TestCase
import datetime
from django.utils import timezone
from django.urls import reverse
from .models import Question
# Create your tests here.
class QuestionTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(),False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now()-datetime.timedelta(days=1,seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(),False)
    
    def test_was_published_recently_with_recent_question(self):
        time = timezone.now()-datetime.timedelta(hours=23,minutes=59,seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(),True)

def create_question(question_text,days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text,pub_date=time)

class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code,200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context['latest_question_list'],[])
    
    def test_past_question(self):
        question = create_question('Question 1',-30)
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context['latest_question_list'], [question])
    
    def test_future_question(self):
        question = create_question('Question 1',30)
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context['latest_question_list'], [])
        
    def test_future_question_and_past_question(self):
        question = create_question('Question 1',-30)
        create_question('Question 2', 30)
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context['latest_question_list'], [question])
    
    def test_two_past_questions(self):
        question1 = create_question('Question 1',-30)
        question2 = create_question('Question 2',-20)
        response = self.client.get(reverse("polls:index"))
        print(response.context['latest_question_list'])  # Debugging line
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context['latest_question_list'], [question2,question1],)
        
    def test_with_no_choices(self):
        question = create_question('Question 1',-30)
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context['latest_question_list'], [question])
        self.assertNotContains(response, 'Choice 1')
        self.assertNotContains(response, 'Choice 2')
    def test_with_choices(self):
        question = create_question('Question 1',-30)
        choice1 = question.choice_set.create(choice_text='Choice 1', votes=0)
        choice2 = question.choice_set.create(choice_text='Choice 2', votes=0)
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context['latest_question_list'], [question])
        self.assertIn(choice1, response.context['latest_question_list'][0].choice_set.all())
        self.assertIn(choice2, response.context['latest_question_list'][0].choice_set.all())
        
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        future_question = create_question('Future question',5)
        url = reverse('polls:detail',args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code,404)
    
    def test_past_question(self):
        past_question = create_question('Past question',-5)
        url = reverse('polls:detail',args=(past_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertContains(response,past_question.question_text)

class QuestionResultsViewTest(TestCase):
    def test_future_question(self):
        future_question = create_question('Future question',5)
        url = reverse('polls:results',args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code,404)
    
    def test_past_question(self):
        past_question = create_question('Past question',-5)
        url = reverse('polls:results',args=(past_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertContains(response,past_question.question_text)

