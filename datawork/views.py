from django.shortcuts import render

from datawork.models import Author, FreeArticle, ProCourses, SubjectField

# Create your views here.

def index(req):
    data={  
        'procourses':ProCourses.objects.all(),
        'freearticle':FreeArticle.objects.all(),
        'author':Author.objects.all(),
        'subjectfield':SubjectField.objects.all(),
    }
    return render(req,'index.html',data)


def cProg(req):
    return render(req, "freecourse/cprog.html")

def proCourse(req,id,slug):
    data={
        'subjectfield':SubjectField.objects.all(),
        'procourse':ProCourses.objects.get(pk=id),
    }
    return render(req,'procourse/procourse.html',data)