from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.conf import settings


# Create your models here.

class Author(models.Model):
    author = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='profilephoto/')

    def __str__(self):
        return self.author


class SubjectField(models.Model):
    field = models.CharField(max_length=200)

    def __str__(self):
        return self.field
    
    

class ProCourses(models.Model):
    course = models.CharField(max_length=200)
    image = models.ImageField(upload_to='course/')
    price = models.FloatField(default=0.0)
    description = models.TextField()
    slug = models.SlugField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    field = models.ForeignKey(SubjectField,on_delete=models.CASCADE)


    def __str__(self):
        return self.course

    def get_absolute_url(self):
        return reverse("datawork:procourses", kwargs={"slug": self.slug})

    def tax_info(self):
        return self.price*0.18

    def total_info(self):
        return self.price + float(self.tax_info())
        



class FreeArticle(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    field = models.ForeignKey(SubjectField, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Coupon(models.Model):
    code = models.CharField(max_length=40)
    discount = models.IntegerField()
    
    def __str__(self):
        return self.code

class OrderedCourses(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    course = models.ForeignKey(ProCourses,on_delete=models.CASCADE,null=True, blank=True )
    ordered = models.BooleanField(default=False)

class Payment(models.Model):
    txn_id = models.CharField(max_length=400)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    amount = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)

    



