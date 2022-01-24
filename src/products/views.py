from django.shortcuts import render, get_object_or_404

from django.http import Http404
from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.
# def product_create_view(request):
#     print(request.GET)
#     print(request.POST)
#     #HOW TO GET USER INFORMATION AND UPDATE DATABASE
#     # my_new_title = request.POST.get('title')
#     # Product.objects.create(title=my_new_title)
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#     context = {
#         'form': form
#     }
#     return render(request, "products/product_create.html", context)

def dynamic_lookup_view(request, my_id):
    # obj = get_object_or_404(Product, id=my_id)
    try: 
        obj = Product.objects.get(id=my_id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)

def product_create_view(request):
    my_form = RawProductForm()
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
            my_form = RawProductForm()
        else:
            print(my_form.errors)
            my_form = RawProductForm()
    context = {
        "form": my_form
    }
    return render(request, "products/product_create.html", context)

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)