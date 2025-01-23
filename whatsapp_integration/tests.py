from rest_framework.test import APITestCase
from unittest.mock import patch
from twilio.rest import Client

# What this test does: It tests the SendWhatsAppMessageView API view by mocking the Twilio API call.
# The test checks if the API view sends a WhatsApp message correctly without actually sending a real message.
class SendWhatsAppMessageTest(APITestCase):
    @patch.object(Client, 'messages')  # Mock the `messages` property on the `Client` object
    def test_send_whatsapp_message(self, mock_messages):
        # Mock the `create` method on the `messages` property
        mock_create = mock_messages.create
        mock_create.return_value.sid = 'SMxxxxxxxxxxxxxxxxxxxxx'

        # Arrange
        url = '/api/send-message/'
        data = {
            "sender": "+14155238886",
            "receiver": "+##########",  # Make sure this is a valid receiver number
            "content": "Running TEST.PY."
        }

        # Make the request
        response = self.client.post(url, data, format='json')

        # Assert the response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('message'), 'Message sent successfully.')
        mock_create.assert_called_once()  # Ensure the mocked Twilio API was called


# This test case actually sends a WhatsApp message using the Twilio API. Good for testing the actual integration.
# class SendWhatsAppMessageTest(APITestCase):
#     def test_send_whatsapp_message(self):
#         url = '/api/send-message/'  # URL of the API endpoint

#         # Data to be sent in the request
#         data = {
#             "sender": "+14155238886",
#             "receiver": "+######",  # Replace with a valid WhatsApp number
#             "content": "Running TEST.PY."
#         }

#         # Make the request
#         response = self.client.post(url, data, format='json')

#         # Log the response to debug
#         print("Response status code:", response.status_code)
#         print("Response data:", response.data)

#         # Check if the response is successful
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.data.get('message'), 'Message sent successfully.')
        