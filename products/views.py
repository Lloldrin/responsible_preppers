from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .forms import ProductForm
from .models import Product, Category


# Create your views here.
def all_products(request):
    
    """This view returns all products, including searches and sorting"""

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'You didn\'t enter any search parameters!')
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(category__friendly_name__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products' : products,
        'search_term' : query,
        'current_categories' : categories,
        'current_sorting' : current_sorting,
    }
    
    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    
    """This view returns the selected product details"""
    template = 'products/product_detail.html'

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product' : product,
    }
    return render(request, template, context)

def add_product(request):

    if request.method == 'POST':
        #Including request.FILES makes sure that we get the images as well as the form data
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Please make sure the form is correct!')
    else: 
        form = ProductForm()

    template = 'products/add_product.html'

    context = {
        'form' : form
    }
    return render(request, template, context)
