from django.contrib import admin
from quiz.models import *



admin.site.register(Quiz)
class AnswerAdmin(admin.StackedInline):
    model = Answer
    

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin,]

admin.site.register(Question , QuestionAdmin)
