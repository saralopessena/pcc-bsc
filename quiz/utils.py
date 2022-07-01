from .forms import AnswerForm

def save_answers (text, is_correct, question):
    answer_form = AnswerForm()

    answer = answer_form.save(commit=False)
    answer.answer = text
    answer.is_correct = is_correct
    answer.question = question
    answer.save()