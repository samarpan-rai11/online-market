from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .models import Item, Category
from .forms import NewItemForm,EditItemForm
# Create your views here.

def items(request):
    query = request.GET.get('Query', '') 
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'item/items.html',{
        'items_search':items,
        's_query': query,   #this 's_query' is needed in value of input tag  so that the query searched won't get deleted after hitting search
        'category':categories,
        'category_id': int(category_id),
    })



#Below this are CRUD operations

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


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)    #this is an object
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]      #this is an object

    return render(request, 'item/detail.html', {
        'ditem': item,
        'related': related_items,
    })


@login_required
def edit(request,pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES,instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:product-detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html',{
        'form': form,
        'title': 'Edit Item',
    })


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')