from time import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, response, Http404, HttpResponseRedirect

from .models import Question 
from .forms import ViewForm
from django.utils import timezone

# Create your views here.

# AFFICHE LE FORM POUR CREER 
def index(request):
    context ={}
 
    form = ViewForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, 'Django_App/index.html', context)
 


# AFFICHE LA LISTE DES QUESTIONS
def list_view(request):
    context ={}
 
    context["dataset"] = Question.objects.all()
         
    return render(request, "Django_App/list_view.html", context)



# AFFICHE QUESTION UNE PAR UNE
def detail_view(request, id):
    context ={}

   
 
    context["data"] = Question.objects.get(id = id)
         
    return render(request, "Django_App/detail_view.html", context)



# PERMET LA MODIFICATION DES QUESTION
def detail_view(request, id):
    context ={}

    context["data"] = Question.objects.get(id = id)
          
    return render(request, "Django_App/detail_view.html", context)
 
def update_view(request, id):
    context ={}
    
    obj = get_object_or_404(Question, id = id)

    form = ViewForm(request.POST or None, instance = obj)
 
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/Django_App/listview/"+id)
 
    context["form"] = form
 
    return render(request, "Django_App/update_view.html", context)



# PERMET LA SUPPRESSION
def delete_view(request, id):
    context ={}
 
    obj = get_object_or_404(Question, id = id)
 
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/Django_App/listview")
 
    return render(request, "Django_App/delete_view.html", context)