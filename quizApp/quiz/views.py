from django.shortcuts import render, redirect
from .models import Quiz, Questions, UserQuizScore
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.

def landing_page(request):
    return render(request, "layout.html")

def quizlist(request):
    quiz_list = Quiz.objects.all()
    return render(request, "quizlist.html", {'quiz_list':quiz_list})

@login_required(login_url="/login/")
def quiz_play(request, quiz_id):

    quiz= get_object_or_404(Quiz,pk=quiz_id)
    questions = Questions.objects.filter(quiz=quiz)

    if request.method=="POST":
        score = 0
        data = request.POST # collecting post data in dict
        keys = list(data.keys()) # Converting dict_keys type to list for slicing
        questions_key=keys[1:]
        for question_id in questions_key: 
            given_answer = data.get(question_id)
            question = get_object_or_404(Questions,pk=question_id)
            if(given_answer==question.correct_option):
                score+=1
        total_question = len(questions_key)
        if UserQuizScore.objects.filter(player=request.user,quiz=quiz):
            user = UserQuizScore.objects.get(player=request.user, quiz=quiz)
            if score>user.score:
                user.score = score
                user.save()
        else:
            user = UserQuizScore.objects.create(player=request.user, quiz=quiz, score=score)
            user.save()
        return render(request,"result.html",{"score":score, "total_questions":total_question,"quiz":quiz})
    
    return render(request, "quiz_play.html",{"questions":questions, "quiz":quiz})

def leaderboard(request,quiz_id):
    quiz = get_object_or_404(Quiz,pk=quiz_id)
    quiz_user = UserQuizScore.objects.filter(quiz=quiz).order_by("-score")
    return render(request,"leaderboard.html",{"quiz":quiz, "quiz_user":quiz_user})
    
def register(request):
    if request.method == "POST":
        data = request.POST
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if(password!=confirm_password):
            messages.error(request,"Re-write Password Correctly!!!")
            return redirect('/register/')

        user_object = User.objects.filter(username=username)
        if(user_object.exists()):
            messages.error(request,"Account Already exist!!!")
            return redirect('/register/')
        
        user_object = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user_object.save()
        auth_login(request,user_object)
        messages.info(request, "Account Created Sucessfully!!!")
        return redirect('register')
    return render(request,"registration/register.html")

def login(request):

    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Successfully logged in...!!!")
            return redirect('landing_page')
        else:
            messages.error(request, "Login Fail...!!!")
            return render(request,'registration/login.html')

    return render(request, "registration/login.html")

def logout(request):
    auth_logout(request)
    messages.error(request, "Successfully Logged out...!!!")
    return redirect('landing_page')

