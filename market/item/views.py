from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Category,Item
from .forms import NewItemForm
# Create your views here.

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)    #this is an object
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]      #this is an object

    return render(request, 'item/detail.html', {
        'ditem': item,
        'related': related_items,
    })

@login_required
def new(request):
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:product-detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html',{
        'form': form,
        'title': 'New Item',
    })
