from django.shortcuts import render,redirect,get_object_or_404

from .models import Choice, Question

# Create your views here.

def home(request):
   questions = Question.objects.all()
   return render(request, 'poll/home.html',
        {"questions": questions})

def vote(request, q_id):
    question = get_object_or_404(Question, pk=q_id)
    if request.method == "POST":
        choice_id = request.POST.get('choice')
        choice = get_object_or_404(Choice, pk=choice_id)
        choice.votes += 1
        choice.save()
        return redirect('poll:result', q_id=q_id)
    return render(request, 'poll/vote.html', {"question": question})

def  result(request, q_id):
    question = get_object_or_404(Question, pk=q_id)
    choice_texts = [choice.choice_text for choice in question.choice_set.all()]
    votes = [choice.votes for choice in question.choice_set.all()]
    
    context = {
        'question': question,
        'choice_texts': choice_texts,
        'votes': votes
    }
    return render(request, 'poll/result.html', context)