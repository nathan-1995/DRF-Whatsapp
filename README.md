
# WhatsApp Integration

Created a basic Django application that allows the user to execute API whatsapp messages (From Twilo) to other whatsapp numbers. Also allows messages from other numbers to be received to the Whatsapp number. All incoming and outgoing messages are saved to the database.

# Demo

## Python Libraries

* Django
* DRF
* Twilio
* Logging
* asyncio

### Features Implemented 
* Send whatsapp message from Twilio to personal number. Gets saved to database
* Send whatsapp message from personal number to Twilio number. Gets saved to database.
* Implemented web hook to receive  incoming whatsapp message
* Logging and error handling.

### Bonus Points
* Setup asynchronous method to send whatsapp message.
* Setup swagger for api documention
* Used github actions to build docker image when changes are pushed to repo.


