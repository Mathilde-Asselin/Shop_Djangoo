from multiprocessing import context
from time import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, response, Http404, HttpResponseRedirect

from .models import Card 
from .forms import CardForm
from .forms import UpdateForm
from django.utils import timezone



# Index -> Affichages des Cards et du form create
def index(request):
    context={}

    form = CardForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form']= form
    context["dataset"] = Card.objects.all().exclude(quantity=0)

    return render(request, 'Shop_App/index.html', context)


def update(request, id):
    context ={}
    
    obj = get_object_or_404(Card, id = id)
    quantity = obj.quantity
    
    form = UpdateForm(request.POST or None, instance = obj)
    if form.is_valid():
        a = form.save(commit=False)
        a.quantity = quantity - obj.quantity 
        a.save()

        return HttpResponseRedirect("/Shop_App")
 
    context["form"] = form
    context["data"] = Card.objects.get(id = id)
 
    return render(request, "Shop_App/update.html", context)