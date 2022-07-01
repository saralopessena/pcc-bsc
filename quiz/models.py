from django.db import models
from posts.models import Posts
import uuid, random
 

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    
    class Meta:
        abstract = True 


class Quiz(BaseModel):
    title = models.CharField(max_length=50)
    description = models.TextField()
    post = models.OneToOneField(Posts, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.title
    


class Question(BaseModel):
    quiz = models.ForeignKey(Quiz,  on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    marks = models.IntegerField(default=5)      
  
    def __str__(self) :
        return self.quiz.title

    def get_answers(self):
        answer_objs = list(Answer.objects.filter(question = self))
        random.shuffle(answer_objs)
        data = []

        for answer_obj in answer_objs:
            data.append({
                'id': answer_obj.uid,
                'answer': answer_obj.answer,
                'is_correct': answer_obj.is_correct
            })
        return data

class Answer(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
 
    def __str__(self):
        return self.question.question