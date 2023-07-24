from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.utils.html import format_html
# class1
class Category(models.Model):
    title = models.CharField(max_length=70,verbose_name="عنوان")
    created = models.DateField(auto_now_add=True,verbose_name="زمان ایجاد")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name="دسته بندی"
        verbose_name_plural="دسته بندی ها"

# class2
class Post(models.Model):
    # Fields
    auther = models.ForeignKey(User , on_delete=models.CASCADE,verbose_name="نویسنده")
    category = models.ManyToManyField(Category , related_name="posts",verbose_name="دسته بندی")
    title = models.CharField(max_length=30,verbose_name="عنوان")
    body = models.TextField(verbose_name="متن")
    image = models.ImageField(upload_to = 'images/posts',verbose_name="تصویر")
    date = models.DateField(auto_now_add=True,verbose_name="زمان تالیف")
    update = models.DateField(auto_now=True,verbose_name="به روز رسانی")
    slug = models.SlugField(null=True , blank=True , unique=True,verbose_name="آدرس")
    class Meta:
        ordering = ('-date',)
        verbose_name = 'پست'
        verbose_name_plural="پست ها"
    # Methods
    def save(self):
        self.slug = slugify(self.title)
        super(Post , self).save()

    def get_absolute_url(self):
        return reverse('post_app:detail' , args=[self.slug])
    def __str__(self):
        return f"{self.title} - {self.body[:30]}"

    def show_img(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="100px" height="90px">')
        else:
            return format_html("<h3>تصویر ندارد</h3>")
    show_img.short_discription="تصویر پست"
class Comment(models.Model):
    article = models.ForeignKey(Post,on_delete=models.CASCADE , related_name='comments',verbose_name="مقاله")
    user = models.ForeignKey(User,on_delete=models.CASCADE , related_name='comments',verbose_name="کاربر")
    parent = models.ForeignKey('self',on_delete=models.CASCADE , related_name='replies', null=True,blank=True)
    body=models.TextField(max_length=300,verbose_name="متن")
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="زمان ایجاد")
    #Methods
    def __str__(self):
        return self.body[:50]
    class Meta:
        verbose_name="نظر"
        verbose_name_plural="نظرات "


class Like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE , related_name='likes',verbose_name="کاربر")
    post=models.ForeignKey(Post,on_delete=models.CASCADE , related_name='likes',verbose_name="پست")
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="زمان ایجاد")

    #Methods
    def __str__(self):
        return f"{self.user} , {self.post}"

    class Meta:
        verbose_name="پسند"
        verbose_name_plural="پسندها "
        ordering = ('created_at',)