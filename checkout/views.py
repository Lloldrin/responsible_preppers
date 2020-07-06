from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrdersForm


# Create your views here.

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'The cart is empty')
        return redirect(reverse('products'))
    
    order_form = OrdersForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form' : order_form,
    }

    return render(request, template, context)

