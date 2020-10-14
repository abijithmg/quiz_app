from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=500)

    def __str__(self):
        return self.question


class Option(models.Model):
    option = models.CharField(max_length=200)

    def __str__(self):
        return self.option


class Round(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name


class Score(models.Model):
    point = models.IntegerField(default=0)
    # trophy = models.CharField(max_length=100)

    def __str__(self):
        return self.point


class Team(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    member = models.ManyToManyField(User)
    score = models.ForeignKey(Score, on_delete=models.CASCADE)    
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class QuizPost(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True)
    option1 = models.ForeignKey(Option, related_name="option1", on_delete=models.CASCADE)
    option2 = models.ForeignKey(Option, related_name="option2", on_delete=models.CASCADE)
    option3 = models.ForeignKey(Option, related_name="option3", on_delete=models.CASCADE)
    option4 = models.ForeignKey(Option, related_name="option4", on_delete=models.CASCADE)
    correct_option = models.IntegerField()
    score = models.ForeignKey(Score, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.question}"

