from django.contrib import admin
from .models import Question, Option, QuizPost, Team


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    pass

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass

@admin.register(QuizPost)
class QuizPostAdmin(admin.ModelAdmin):
    pass