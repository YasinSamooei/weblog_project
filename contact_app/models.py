from operator import mod
from ssl import create_default_context
from turtle import title
from django.db import models

class Massage(models.Model):
    title=models.CharField(max_length=100,verbose_name="عنوان")
    text=models.TextField(verbose_name="متن")
    email=models.EmailField(verbose_name="ایمیل")
    def __str__(self):
        return (self.title)
    class Meta:
        verbose_name="پیام"
        verbose_name_plural="پیام ها"