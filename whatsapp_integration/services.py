from twilio.rest import Client
from django.conf import settings
from .models import WhatsAppMessage
import logging
import uuid
import asyncio

# Set up logging
logger = logging.getLogger(__name__)

# Function to send a WhatsApp message
def send_whatsapp_message(sender, receiver, content):

    # Generate a unique request ID
    request_id = str(uuid.uuid4())
    logger.info(f"Request ID: {request_id} - Sending WhatsApp message from {sender} to {receiver} with content: {content}")

    try:
        # Set up the Twilio client
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

        # Send the WhatsApp message
        message = client.messages.create(
            from_=f"whatsapp:{sender}",
            to=f"whatsapp:{receiver}",
            body=content
        )

        logger.info(f"Request ID: {request_id} - Message sent successfully with SID: {message.sid}")

        # Save to database
        save_message_to_db(sender, receiver, content, status='sent')

        return {"success": True, "message_sid": message.sid}

    except Exception as e:
        logger.error(f"Request ID: {request_id} - Failed to send message: {e}")

        # Save to the database
        save_message_to_db(sender, receiver, content, status='failed')

        return {"success": False, "error": str(e)}


# Async function to call the synchronous method. This allows the synchronous method to run in a separate thread.
async def send_whatsapp_message_async(sender, receiver, content):

    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, send_whatsapp_message, sender, receiver, content)

# Function to save WhatsApp message to the database
def save_message_to_db(sender, receiver, content, status):
    """
    Helper function to save WhatsApp message to the database.
    """
    try:
        WhatsAppMessage.objects.create(
            sender=sender,
            receiver=receiver,
            content=content,
            status=status
        )
        logger.info(f"Message saved to database: sender={sender}, receiver={receiver}, status={status}")
    except Exception as e:
        logger.error(f"Error saving message to database: {e}")
