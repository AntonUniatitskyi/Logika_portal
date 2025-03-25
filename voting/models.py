from django.db import models
from django.contrib.auth.models import User

class Poll(models.Model):
    question = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll, related_name="choices", on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    votes_count = models.PositiveIntegerField(default=0)  # Кеш голосів

    def __str__(self):
        return self.text

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    voted_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'poll')  # Користувач може голосувати лише раз

    def save(self, *args, **kwargs):
        if self.pk:  # Якщо редагується існуючий голос
            old_vote = Vote.objects.get(pk=self.pk)
            if old_vote.choice != self.choice:
                old_vote.choice.votes_count -= 1
                old_vote.choice.save()
        else:
            self.choice.votes_count += 1
            self.choice.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.choice.votes_count -= 1
        self.choice.save()
        super().delete(*args, **kwargs)