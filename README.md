
# WhatsApp Integration

Created a basic Django application that allows the user to execute API whatsapp messages (From Twilo) to other whatsapp numbers. Also allows messages from other numbers to be received to the Whatsapp number. All incoming and outgoing messages are saved to the database.

# Demo

Live hosting of the source code can be found here. 
http://34.72.205.69:8000/api/docs/swagger/

# Screenshots

![image](https://github.com/user-attachments/assets/9a7ebfa5-25af-4539-83c3-4b7730ddb17a)

![image](https://github.com/user-attachments/assets/304cb642-3ca1-4800-b0a9-e9277e43907c)

![image](https://github.com/user-attachments/assets/7cb65a87-3b72-435b-b9c3-bdfcd01b211d)

![image](https://github.com/user-attachments/assets/02e31d52-0e43-487c-a4d6-e299ce0e6111)


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
* Added basic test case

### Bonus Points
* Setup asynchronous method to send whatsapp message.
* Setup swagger for api documention
* Used github actions to build docker image when changes are pushed to repo.


