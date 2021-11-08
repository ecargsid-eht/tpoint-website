from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from datawork.models import *
from django.contrib.auth.decorators import login_required

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
    course = OrderedCourses.objects.filter(user = req.user,course = ProCourses.objects.get(pk=id),ordered=True)
    data={
        'subjectfield':SubjectField.objects.all(),
        'procourse':ProCourses.objects.get(pk=id),
        'coursebought':OrderedCourses.objects.filter(user = req.user, ordered = True)
    }
    if course.exists():
        return render(req,'procourse/ordered.html',data)
    else:
        return render(req,'procourse/procourse.html',data)

@login_required
def orderCourse(req,id):
    order = OrderedCourses.objects.create(user=req.user,ordered = False)
    order.course = ProCourses.objects.get(pk=id)
    order.save()
    return render(req,'payment.html')

@login_required
def myCourse(req):
    data = {
        'mycourse':OrderedCourses.objects.filter(user = req.user, ordered=True)
    }
    return render(req,'mycourse.html',data)

def ordered(req):
    order = OrderedCourses.objects.get(user=req.user, ordered=False)
    order.ordered = True
    print(order.course)
    # order.ordered = True
    order.save()
    return redirect (index)

def payment(req):
    order = OrderedCourses.objects.get(user=req.user, ordered=False)
    print(order.course)
    order.ordered = True
    order.save()
    return redirect(index)
