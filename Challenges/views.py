from itertools import product
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from requests import post
from Challenges.forms import PostForm, CommentForm
from .models import Post, Comment
from django.utils import timezone
from django.contrib.auth.models import User

def challenge(request, pk):
    global comments
    data = Post.objects.get(id = pk)
    print(f"____________The products id is {pk}+_______________")
    hackingChallenege = Post.objects.all()
    username = None
    if request.user.get_username():
        username = request.user.username
        print(f"____________This is {username}+_______________")
    if request.method == "POST":
        form = CommentForm(request.POST)
        print(form)
        if form.is_valid():
            print(f"____________YEAHHH FORM IS VALID_______________")
            name = username
            comments = form.cleaned_data['comments']
            dt = Comment(name= name, comments= comments, post = data)
            dt.save()
            print(f"____________YEAHHH FORM IS CREATED_______________")
            return HttpResponseRedirect(f'/challenges/{pk}/challengeInfo')
    else:
        form = CommentForm()
        comments = Comment.objects.filter(post = data)
        replies = Comment.objects.filter(post = data)

    for i in hackingChallenege:
        if i.id == pk:
            hackingChallenegeTitle = i.title
            hackingChallenegeInfo = i.description

    return render(request, 
                'challenge.html', 
                {'hackingChallenegeTitle': hackingChallenegeTitle,
                'hackingChallenegeInfo': hackingChallenegeInfo,
                'data':data,
                'form':CommentForm,
                'comment': comments,
                })

@login_required
def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            print('_______________Form INvalid__________ ')
            return render (request, 'create.html', {'error': 'All fields required'})    
    else:
        return render (request, 'create.html')

@login_required
def comment(request):
    if request.method == "POST":
        if request.POST['comment']:
            myComment = Comment()
            myComment.title = request.user
            myComment.comment = request.POST['comment']
            myComment.save()
            return redirect('homePage')
        else:
            return render (request, 'create.html', {'error': 'All fields required'})    
    else:
        return render (request, 'create.html')
