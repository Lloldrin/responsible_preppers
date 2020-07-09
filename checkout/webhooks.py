from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import StripeWH_Handler

import stripe

# This page closely follows Stripes webhook guide found here: https://stripe.com/docs/webhooks?lang=python with modifications to follow the CodeInstitute coursework.

@require_POST
@csrf_exempt
def webhook(request):
    # This listens to webhooks coming from Stripe

    # API and Secret Keys. These are placed in the environment for security
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Reads the data sent from the webhook and verifies the signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
        payload, sig_header, wh_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
        # General exeptions not covered by payload or signature
    except Exception as e:
        return HttpResponse(content=e, status=400)

    print('success')
    return HttpResponse(status=200)

    # This sets up the webhook handler
    handler = StripeWH_Handler(request)

    # This maps webhook events to the relevant handler functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
    }

    # Gets the type of webhook from Stripe
    event_type = event['type']

    # If there's a handler for it, get it from the event map
    # Use the generic one by default
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call the event handler with the event
    response = event_handler(event)
    return response