from django.shortcuts import redirect, render
from .models import Product
from django.http import HttpResponse
from .forms import ProductForm
# Create your views here.

def product_list(request):
    products = Product.objects.all()
    context = { 'product_list': products }
    return render(request, 'index.html', context)

def product_details(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'index2.html', context)

def edit_product(request, pk):
    product = Product.objects.get(id = pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance = product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit.html', {'form' : form})

def delete_product(request, pk):
    product = Product.objects.get(id = pk)
    if request.method == "POST":
        product.delete()
        return redirect('product_list')
    else:
        context = {'product':product}
        return render(request, 'delete.html', context)
    
def home(request):
    return HttpResponse("Hello World!")