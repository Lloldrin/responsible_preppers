from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from decimal import Decimal

def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({
            'item_id' : item_id,
            'quantity' : quantity,
            'product' : product,
        })

    if total < settings.FREE_SHIPPING_TRESHOLD:
        shipping = total * Decimal(settings.STANDARD_SHIPPING_PERCENTAGE / 100)
        free_shipping_remaining = settings.FREE_SHIPPING_TRESHOLD - total
    else:
        shipping = 0
        free_shipping_remaining = 0

    grand_total = total + shipping


    context = {

        'cart_items' : cart_items,
        'product_count' : product_count,
        'shipping' : shipping,
        'free_shipping_remaining' : free_shipping_remaining,
        'free_shipping_treshhold' : settings.FREE_SHIPPING_TRESHOLD,
        'total' : total,
        'grand_total' : grand_total, 

    }

    return context