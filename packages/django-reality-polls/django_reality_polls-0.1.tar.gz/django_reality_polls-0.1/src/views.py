from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Question,Choice
from .forms import QuestionForm
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

def vote(request,question_id):
    q = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = q.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{
            'question':q,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        
    return HttpResponseRedirect(reverse('polls:results',args=(q.id,)))

def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.pub_date = timezone.now()
            question.save()

            # Handle choices
            choice1_text = request.POST.get('choice1')
            choice2_text = request.POST.get('choice2')
            correct_answer = request.POST.get('correct_answer')

            if choice1_text and choice2_text and correct_answer:
                Choice.objects.create(question=question, choice_text=choice1_text, votes=0)
                Choice.objects.create(question=question, choice_text=choice2_text, votes=0)

                # Add more choices as needed based on dynamic inputs
                for i in range(3, 11):  # Assuming max 10 choices
                    choice_text = request.POST.get(f'choice{i}')
                    if choice_text:
                        Choice.objects.create(question=question, choice_text=choice_text, votes=0)

            return redirect('polls:index')  # Redirect to the polls index page
    else:
        form = QuestionForm()
    return render(request, 'polls/add_question.html', {'form': form})
