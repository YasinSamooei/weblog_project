from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
    user = models.OneToOneField(User , on_delete= models.CASCADE,verbose_name="کاربر")
    fatherName = models.CharField(max_length=30,verbose_name="نام پدر")
    natunalCode = models.CharField(max_length=10,verbose_name="کد ملی")
    image = models.ImageField(upload_to = "profiles/images" , blank = True , null = True,verbose_name="تصویر")
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name="پروفایل"
        verbose_name_plural="پروفایل ها"