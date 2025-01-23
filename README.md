[Setup](#How-to-setup)

[Screenshots](#screenshots)

[Python Libraries)](#Python-Libraries)

[Features Implemented](#Features-Implemented)

[Bonus](#Bonus)
 

# WhatsApp Integration

Created a basic Django application that allows the user to execute API whatsapp messages (From Twilo) to other whatsapp numbers. Also allows messages from other numbers to be received to the Whatsapp number. All incoming and outgoing messages are saved to the database.

# Demo

Live hosting of the source code can be found here. 
http://34.72.205.69:8000/api/docs/swagger/

Disclaimer:
The app uses a free/unverified Twilio account, which may result in rate-limiting errors (Twilio 429) due to too many requests within a short period.

# How to setup
## WhatsApp Integration API - Local Setup and Installation


#### Step 1
First, clone the repository to your local machine.
Open Terminal and run these commands:
```bash
git clone https://github.com/nathan-1995/DRF-Whatsapp.git
```
```bash
cd DRF-Whatsapp
```
```bash
python -m venv venv
```
```bash
pip install -r requirements.txt
```

#### Step 2:
Create a .env file in the project root and add your Twilio credentials:

`TWILIO_ACCOUNT_SID=your_account_sid`

`TWILIO_AUTH_TOKEN=your_auth_token`

`TWILIO_PHONE_NUMBER=your_twilio_phone_number`

#### Step 3:
Run and make sure all necessary migrations are created and applied:
```bash
python manage.py migrate
```
And create a superuser:
```bash
python manage.py createsuperuser
```
#### Step 4:
Launch django:
```bash
python manage.py runserver
```
Head to:
```bash
http://localhost:8000
```

# Screenshots

![image](https://github.com/user-attachments/assets/9a7ebfa5-25af-4539-83c3-4b7730ddb17a)

![image](https://github.com/user-attachments/assets/abc6ed67-1c1b-4076-8e5e-0a4f9089b0e3)

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

### Bonus
* Setup asynchronous method to send whatsapp message.
* Setup swagger for api documention
* Used github actions to build docker image when changes are pushed to repo.


### Design Decisions
* Twilio API: Twilio is used for WhatsApp messaging because it provides an easy to use API, webhook and easy to implement.
* CI/CD Setup: GitHub Actions is set up for automatic Docker image builds and deployments to Docker Hub.
* Dockerization:  Making it easier to deploy anywhere. 

