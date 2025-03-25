from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Poll, Question, Choice, Vote
from django.db import transaction

@login_required
def poll_list(request):
    polls = Poll.objects.all()
    user_votes = Vote.objects.filter(user=request.user).values_list("choice__question__poll_id", flat=True)
    
    return render(request, 'voting/poll_list.html', {
        'polls': polls,
        'user_votes': user_votes,
        'is_admin': request.user.is_staff
    })

@login_required
def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    return render(request, 'voting/poll_detail.html', {'poll': poll})

@login_required
def vote(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)

    if request.method == 'POST':
        for question in poll.questions.all():
            choice_id = request.POST.get(f'question-{question.id}')
            if choice_id:
                choice = Choice.objects.get(id=choice_id)
                Vote.objects.update_or_create(user=request.user, choice=choice)

        return redirect('voting:poll_list')

    return render(request, 'voting/poll_detail.html', {'poll': poll})

@login_required
def create_poll(request):

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        questions = request.POST.getlist("question")
        choices_list = request.POST.getlist("choices")

        with transaction.atomic():
            poll = Poll.objects.create(title=title, description=description, created_by=request.user)

            for i, question_text in enumerate(questions):
                if question_text.strip():
                    question = Question.objects.create(poll=poll, text=question_text)
                    
                    choices = choices_list[i].split(";")  # Варіанти відповідей розділяємо ";"
                    for choice_text in choices:
                        if choice_text.strip():
                            Choice.objects.create(question=question, text=choice_text)

        return redirect('voting:poll_list')

    return render(request, 'voting/create_poll.html')