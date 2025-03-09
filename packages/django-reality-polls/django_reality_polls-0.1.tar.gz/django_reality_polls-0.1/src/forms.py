from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    question_text = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your question here'
        })
    )

    class Meta:
        model = Question
        fields = ['question_text']
