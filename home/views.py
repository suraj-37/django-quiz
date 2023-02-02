from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from .models import *
import random

# Create your views here.
def home(request):
    context= {'categories' : Category.objects.all()}

    if request.GET.get('category'):
        return redirect(f"/quiz/?category={request.GET.get('category')}")

    return render(request,'home.html' , context)

def quiz(request):
     return render (request, 'quiz.html')


def getQuiz(request):
    try:
        question_objs=(Question.objects.all())
        
        if request.GET.get('category'):
            question_objs = question_objs.filter(Category__category_name__icontains=request.Get.get('category'))
        question_objs=list(question_objs) 
        random.shuffle(question_objs)
        data =[]
        for question_obj in question_objs:
            data.append({
                "category":question_obj.category.Category_name,
                "question":question_obj.question,
                "marks":question_obj.marks,
                "answers":question_obj.get_answers()
            })
        
        payload={'status':True, 'data':data}

        return JsonResponse(payload)
        

    except Exception as e:
        print(e)
        return HttpResponse("something went wrong")
