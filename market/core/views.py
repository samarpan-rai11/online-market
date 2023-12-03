from django.shortcuts import render, redirect

from item.models import Category,Item
from .forms import SignUpForm
# Create your views here.

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]  #this is an object
    categories = Category.objects.all()  #this is an object

    return render(request, 'core/index.html', {
        'categories' : categories,
        'items' : items, 
    })


def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignUpForm()     #this is an object 
        
    return render(request, 'core/signup.html', {
        'form': form
    })