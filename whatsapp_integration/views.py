import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import send_whatsapp_message_async
from .models import WhatsAppMessage
import asyncio
from .schema import send_whatsapp_message_schema



# Set up logging
logger = logging.getLogger('whatsapp_integration')

# Redirect root URL to the Swagger UI
def redirect_to_swagger(request):
    return redirect('/api/docs/swagger/')

# View to send WhatsApp messages using the Twilio API
@send_whatsapp_message_schema # Apply the schema to the view
class SendWhatsAppMessageView(APIView):
    def post(self, request):
        # Log the request data
        logger.info(f"Received request data: {request.data}")

        # Extract data from request body
        sender = request.data.get('sender')
        receiver = request.data.get('receiver')
        content = request.data.get('content')

        logger.info(f"Received message send request: sender={sender}, receiver={receiver}, content={content}")

        # Validate input data
        if not sender or not receiver or not content:
            logger.warning("Invalid data received in send-message API.")
            return Response(
                {"error": "sender, receiver, and content are required fields."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Sends the message asynchronously using the send_whatsapp_message_async function from services.py.
            # This function wraps the synchronous send_whatsapp_message function, which sends the WhatsApp message
            # via the Twilio API. By using the async wrapper, the operation runs in the background,
            # allowing the view to handle other requests without being blocked while waiting for the message to be sent.

            response = asyncio.run(send_whatsapp_message_async(sender, receiver, content))

            if response["success"]:
                logger.info(f"Message sent successfully: message_sid={response['message_sid']}")
                return Response(
                    {"message": "Message sent successfully.", "message_sid": response["message_sid"]},
                    status=status.HTTP_200_OK
                )
            else:
                logger.error(f"Failed to send message: {response['error']}")
                return Response(
                    {"error": "Failed to send message.", "details": response["error"]},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        except Exception as e:
            logger.error(f"Error processing send message request: {e}")
            return Response(
                {"error": "An error occurred while sending the message."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


# Webhook to handle incoming WhatsApp messages from Twilio and log them in the database
@csrf_exempt
def twilio_webhook(request):
    if request.method == 'POST':
        try:
            # Parse incoming data from Twilio
            data = request.POST
            sender = data.get('From', '')
            receiver = data.get('To', '')
            content = data.get('Body', '')

            logger.info(f"Incoming message received: sender={sender}, receiver={receiver}, content={content}")

            # Save the message to the database
            WhatsAppMessage.objects.create(
                sender=sender,
                receiver=receiver,
                content=content,
                status='received'
            )

            logger.info("Message successfully logged in the database.")
            return JsonResponse({"message": "Message received successfully."}, status=200)
        except Exception as e:
            logger.error(f"Error processing webhook: {e}")
            return JsonResponse({"error": str(e)}, status=400)
    else:
        logger.warning("Invalid request method for webhook.")
        return JsonResponse({"error": "Invalid request method."}, status=405)
