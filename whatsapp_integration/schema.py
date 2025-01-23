from drf_spectacular.utils import extend_schema

# Schema for SendWhatsAppMessageView
send_whatsapp_message_schema = extend_schema(
    summary="Send WhatsApp Message",
    description=(
        "Sends a WhatsApp message using the Twilio API.The operation is logged and saved to the database.\n\n"
        "The sender, receiver, and content are required fields.\n\n"
        "The sender number is the twilio number. Message the Send number with **join believed-highway** to get your number into the sandbox.\n\n"
        "The receiver number should change to your number to receive the message.\n\n"
    ),
    request={
        "application/json": {
            "type": "object",
            "properties": {
                "sender": {"type": "string", "description": "The sender's WhatsApp number, e.g., '+14155238886'"},
                "receiver": {"type": "string", "description": "The receiver's WhatsApp number, e.g., '+94770541166'"},
                "content": {"type": "string", "description": "The message content, e.g., 'Hello, this is a test message.'"},
            },
            "required": ["sender", "receiver", "content"],
            "example": {
                "sender": "+14155238886",
                "receiver": "+94770541166",
                "content": "Hello, this is a test message from Twilio Whatsapp."
            },
        }
    },
    responses={
        200: {
            "description": "Message sent successfully",
            "examples": {
                "application/json": {
                    "message": "Message sent successfully.",
                    "message_sid": "SMxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                }
            }
        },
        400: {"description": "Invalid input data"},
        500: {"description": "Internal server error while sending the message"},
    },
)
