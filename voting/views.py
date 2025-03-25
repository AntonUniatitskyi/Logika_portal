from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Poll, Choice, Vote

# Шаблон для списку опитувань
@login_required
def poll_list(request):
    polls = Poll.objects.all()
    return render(request, 'voting/poll_list.html', {'polls': polls})

# Шаблон для деталей опитування
@login_required
def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    choices = poll.choices.all()
    user_vote = Vote.objects.filter(user=request.user, poll=poll).first()

    if request.method == 'POST':
        choice_id = request.POST.get('choice')
        choice = get_object_or_404(Choice, id=choice_id)

        if user_vote:
            user_vote.choice = choice
            user_vote.save()
        else:
            Vote.objects.create(user=request.user, poll=poll, choice=choice)

        return redirect('voting:poll_results', poll_id=poll.id)

    return render(request, 'voting/poll_detail.html', {'poll': poll, 'choices': choices, 'user_vote': user_vote})

# Шаблон для результатів опитування
@login_required
def poll_results(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    return render(request, 'voting/poll_results.html', {'poll': poll})

# Для кроку опитування учнів (перша сторінка)
@login_required
def poll_step(request):
    if request.method == "POST":
        request.session["dob"] = request.POST.get("dob")  # Дата народження
        request.session["lessons"] = request.POST.getlist("lessons")  # Улюблені уроки
        return redirect("voting:poll_final")  # Перехід на фінальну сторінку

    return render(request, "voting/poll_list.html")  # Використовуємо poll_list.html

# Для фінальної сторінки опитування учнів
@login_required
def poll_final(request):
    if request.method == "POST":
        request.session["career"] = request.POST.get("career")
        return redirect("/")  # Повернення на головну

    return render(request, "voting/poll_final.html")  # Використовуємо poll_final.html