from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, Comment, Answer
from .forms import CommentForm, AnswerForm, QuestionForm, SignUpForm, LoginForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def landing(request):
    return render(request,"landing.html")

def top_questions(request):
    questions = Question.objects.all()
    return render(request, 'top_questions.html', {'questions': questions})

def question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = Answer.objects.filter(question=question)
    
    comments = Comment.objects.filter(answer__in=answers)
    
    if request.method == 'POST':
        if 'comment' in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.answer = Answer.objects.get(pk=request.POST.get('answer_id'))
                comment.author = request.user
                comment.save()
                return redirect('question', pk=pk)
        elif 'answer' in request.POST:
            form = AnswerForm(request.POST)
            if form.is_valid():
                answer = form.save(commit=False)
                answer.question = question
                answer.author = request.user
                answer.save()
                return redirect('question', pk=pk)
    
    comment_form = CommentForm()
    answer_form = AnswerForm()
    
    context = {
        'question': question,
        'answers': answers,
        'comments': comments,
        'comment_form': comment_form,
        'answer_form': answer_form,
    }
    return render(request, 'question.html', context)

def add_comment(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.answer = answer
            comment.author = request.user
            comment.save()
            return redirect('question', pk=answer.question.pk)
    return redirect('question', pk=answer.question.pk)

def add_answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            return redirect('question', pk=question.pk)
    return redirect('question', pk=question.pk)

@login_required
def ask_question(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        if title and body:
            Question.objects.create(
                title=title,
                body=body,
                author=request.user
            )
            return redirect('top_question')
    return render(request, 'ask_question.html')

def submit_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('top_question')
    else:
        form = QuestionForm()
    
    return render(request, 'ask_question.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('landing')

@login_required
def home(request):
    return render(request, 'landing.html')