from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render, redirect
from .models import Quiz, Question
from .utils import save_answers
from posts.models import Posts
from .forms import QuizForm, QuestionForm, AnswerForm
from django.core.exceptions import ObjectDoesNotExist

@login_required(login_url=settings.LOGIN_URL)
def create_question(request, quiz_id):
    quiz = Quiz.objects.get(uid=quiz_id)

    if request.method == 'POST':
        question_form = QuestionForm(request.POST)

        answers = []
        answer_correct = int(request.POST['answer_correct'])

        for i in range(5):
            if i + 1 == answer_correct:
                answers.append({
                    'answer': request.POST['answer' + str(i + 1)],
                    'is_correct': True
                })
            else:
                answers.append({
                    'answer': request.POST['answer' + str(i + 1)],
                    'is_correct': False
                })

        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.quiz = quiz
            question.save()
     
            for i in range(5):
                save_answers(
                    answers[i]['answer'],
                    answers[i]['is_correct'],
                    question
                    )
        else:
            return HttpResponse('<h1>Não foi possível criar posts</h1>')
    else:   
        question_form = QuestionForm(request.POST)

    context = {
        'question_form': question_form,
        'quiz': quiz
    }
    return render(request, 'create_question.html', context)

@login_required(login_url=settings.LOGIN_URL)
def create_quiz(request, posts_id):
    post = Posts.objects.get(id=posts_id)

    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.post = post
            quiz.save()
            return redirect('quiz:create-question', quiz.uid)
        else:
            return HttpResponse('<h1>Não foi possível criar posts</h1>')
    else:   
        form = QuizForm()
        return render(request, 'create_quiz.html', {'form': form})

def list_quiz(request, posts_id):
    try:
        if request.method == "GET":
            quiz = Quiz.objects.get(post=posts_id)
            qtd = Question.objects.filter(quiz=quiz.uid)
            print(len(qtd))
            context = {
                'quiz': quiz,
                'qtd': len(qtd),
            
            }
        return render(request, 'list_quiz.html', context)
    except Quiz.DoesNotExist:
        return HttpResponseNotFound({'O Post ainda não possui Quiz criado'})


def get_uuid_post(request, posts_id):
    quiz = Quiz.objects.get(post=posts_id)
    return HttpResponse(quiz.uid)

def get_quiz(request, quiz_id, posts_id):

    try:
        if request.method == "GET":
            question_objs = list(Question.objects.filter(quiz=quiz_id)) 
            data = []

            for question_obj in question_objs:
                data.append({
                    'id': question_obj.uid,
                    'quiz': question_obj.quiz.title,
                    'question': question_obj.question,
                    'marks': question_obj.marks,
                    'answer': question_obj.get_answers()    
                })
            payload = {
                'data': data
            } 
            data = JsonResponse(payload)
            return HttpResponse(data)
        else:
            pass
    except ObjectDoesNotExist:
        context = {
            'question_objs': question_objs
        }
        return HttpResponse({'content':'Objeto não encontrado'}, context)
    except Exception as err:
        print(err)
        return HttpResponse('Algo deu errado')


@login_required(login_url=settings.LOGIN_URL)
def delete_question(request, question_id):
    Question.objects.get(id=question_id).delete()
    return redirect('/')