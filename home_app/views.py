from django.shortcuts import render
from post_app.models import Post
def home(request):
    recent_articles = Post.objects.all().order_by('-date')[:3]
    article = Post.objects.all()
    
    return render(request , "home_app/index.html" ,{'article':article , 'recent_articles':recent_articles })
