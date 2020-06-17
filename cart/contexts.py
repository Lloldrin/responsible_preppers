from django.conf import settings
from decimal import Decimal

def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0

    if total < settings.FREE_SHIPPING_TRESHOLD:
        shipping = Decimal(settings.STANDARD_SHIPPING_PERCENTAGE)
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