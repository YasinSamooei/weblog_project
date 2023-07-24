from django.urls import path
from .  import views
app_name = "post_app"
urlpatterns = [
    path("detail/<slug:slug>" , views.PostDetailView.as_view() , name = "detail"),
    path("list" , views.Post_list.as_view() , name = "list"),
    path("category/<int:pk>",views.category_dtail,name="category_detail"),
    path("search/" , views.search , name = "search"),
    path("like/<slug:slug>/<int:pk>",views.like,name="like")
]