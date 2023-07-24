from django.contrib import admin
from .models import Post , Category,Comment,Like
#---------------------------------------------------------------------
#costomies filters:
class TitleFilter(admin.SimpleListFilter):
    title="بر اساس کلمات پرتکرار"
    parameter_name="title"
    def lookups(self, request, model_admin):
        return (
            ("python","پایتون"),
            ("django","جنگو"),
        )
    def queryset(self, request, queryset) :
        if self.value():
            return queryset.filter(title__icontains=self.value())

#---------------------------------------------------------------------
class CommentInline(admin.TabularInline):
    model=Comment


@admin.register(Post)
class PostField(admin.ModelAdmin):
    list_display= ("__str__","auther","show_img")
    list_filter=["category",TitleFilter]
    search_fields=["title","body"]
    inlines=[CommentInline]
#----------------------------------------------------------------------
#admin_registers
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Like)
#--------------------------------------------------------------------
admin.site.site_header="مدیریت وبلاگ"