from django.shortcuts import render
from Challenges.models import Post

def homePage(request):
    hackingChallenege = Post.objects.all()
    return render(request, 'home.html', {
                            'hackingChallenege': hackingChallenege,
                            })