from post_app.models import Post , Category
def recent_post(request):
    recent_posts = Post.objects.all().order_by('-date')[:3]
    categoris = Category.objects.all()
    return{"recent_posts":recent_posts , "categoris":categoris}