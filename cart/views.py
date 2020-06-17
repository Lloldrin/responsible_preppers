from django.shortcuts import render

# Create your views here.
def view_cart(request):
    
    """This view returns the cart page"""
    return render(request, 'cart/cart.html')
