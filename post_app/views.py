#imports
from django.http import JsonResponse
from django.shortcuts import redirect, render , get_object_or_404
from .models import Like, Post , Category,Comment
from django.core.paginator import Paginator
from django.views.generic import ListView,DetailView
from .mixins import LoginRequire
#-------------------------------------------------------------------

# function base view
def post_detail(request , slug):
    post = get_object_or_404(Post , slug = slug)
    if request.method=='POST':
        body=request.POST.get('body')
        parent_id= request.POST.get('parent_id')
       
        
        Comment.objects.create(article=post,user=request.user,parent_id=parent_id,body=body)
    return render (request , "post_app/post-details.html" , {'post':post})

#class base view
class PostDetailView(DetailView):
    model=Post
    template_name="post_app/post-details.html"
    def get_context_data(self,**kwargs):
        if self.request.user.is_authenticated:
            context= super().get_context_data(**kwargs)
            if self.request.user.likes.filter(post__slug=self.object.slug,user_id=self.request.user.id).exists():
                context["liked"]=True
            else:
                context["liked"]=False
            return context
        else:
            context= super().get_context_data(**kwargs)
            context["liked"]=False
            return context
#-------------------------------------------------------------------

# function base view
def post_list(request):
    articles = Post.objects.all()
    paginator= Paginator(articles,3)
    page_number=request.GET.get('page')
    objects_list=paginator.get_page(page_number)
    return render (request , "post_app/blog.html" , {'article':objects_list})

#class base view
class Post_list(LoginRequire,ListView):
    model= Post
    context_object_name= "article"
    template_name= "post_app/blog.html"
    paginate_by= 4

#-------------------------------------------------------------------


def category_dtail(request , pk = None):
    category = get_object_or_404(Category , id = pk)
    articles = category.posts.all()
    return render (request , "post_app/blog.html" , {'article':articles})
#-------------------------------------------------------------------


def search(request):
    q=request.GET.get('q')
    posts=Post.objects.filter(title__icontains=q)
    paginator= Paginator(posts,1)
    page_number=request.GET.get('page')
    objects_list=paginator.get_page(page_number)
    return render(request , "post_app/blog.html" ,{'article':objects_list})
#-------------------------------------------------------------------

def like(request,slug,pk):
    if request.user.is_authenticated:
        try:
            like=Like.objects.get(post__slug=slug,user_id=request.user.id)
            like.delete()
            return JsonResponse({"response":"unliked"})
        except:
            Like.objects.create(post_id=pk,user_id=request.user.id)
            return JsonResponse({"response":"liked"})
    else:
        return redirect("acount_app:login")