from django.shortcuts import render, get_object_or_404
from .models import Category,Item
# Create your views here.

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)    #this is an object
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]      #this is an object

    return render(request, 'item/detail.html', {
        'item1': item,
        'related_items': related_items
    })