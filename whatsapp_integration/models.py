from django.db import models

# Create your models here.

#Model for storing WhatsApp messages
class WhatsAppMessage(models.Model):
    STATUS_CHOICES = [
        ('sent', 'Sent'),
        ('received', 'Received'),
        ('failed', 'Failed'),
    ]

    sender = models.CharField(max_length=50)  # Phone number of the sender
    receiver = models.CharField(max_length=50)  # Phone number of the receiver
    content = models.TextField()  # Message content
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically set when the message is created
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='sent')  # Message status

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver} at {self.timestamp}"

