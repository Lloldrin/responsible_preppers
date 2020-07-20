from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


# Create your views here.


def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated Successfully!')
        else: 
            messages.error(request, 'Please make sure you filled the form out correctly')
    else:
        # Displays the users profile.
        form = UserProfileForm(instance=profile)
    
    # Displays the users previous orders
    orders = profile.orders.all()
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    order_date = order.date.date()

    messages.info(request, (
        f'Order: {order_number} had a confirmation e-mail sent on: {order_date} '
        
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
