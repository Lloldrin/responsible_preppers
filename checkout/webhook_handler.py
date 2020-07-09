from django.http import HttpResponse


class StripeWH_Handler:
    #This is the handler for the Stripe Webhooks

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        #Run if the webhook is generic or unknown
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        #Run if the webhook comes back as payment_intent_succeeded
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        #Run if the webhook comes back as payment_intent.payment_failed
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)