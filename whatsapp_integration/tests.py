from rest_framework.test import APITestCase

class SendWhatsAppMessageTest(APITestCase):
    def test_send_whatsapp_message(self):
        url = '/api/send-message/'  # URL of the API endpoint

        # Data to be sent in the request
        data = {
            "sender": "+14155238886",
            "receiver": "+######",  # Replace with a valid WhatsApp number
            "content": "Running TEST.PY."
        }

        # Make the request
        response = self.client.post(url, data, format='json')

        # Log the response to debug
        print("Response status code:", response.status_code)
        print("Response data:", response.data)

        # Check if the response is successful
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('message'), 'Message sent successfully.')
        