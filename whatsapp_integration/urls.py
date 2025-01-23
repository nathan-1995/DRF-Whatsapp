from django.urls import path
from .views import SendWhatsAppMessageView, twilio_webhook, redirect_to_swagger

urlpatterns = [
    path('send-message/', SendWhatsAppMessageView.as_view(), name='send_whatsapp_message'),
    path('webhook/twilio/', twilio_webhook, name='twilio_webhook'),
    path('', redirect_to_swagger),  # Redirect to swagger page

]
