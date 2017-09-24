# Django-cloud

This app allows the user to upload their songs,video,documents to the cloud server.

### Prerequisites

What things you need to install the software and how to install them

```
1. pip install Django==1.9
2. pip install django-admin
```


Steps to follow:

```
1. django-admin startproject website
2. python manage.py startapp music
3. python manage.py makemigrations
4. python manage.py migrate
5. Migrations will be used just in context of model creations only.
6. python manage.py runserver
```
#Deploy on ngrok:
```
1. Download the ngrok zip file.
2. Open the terminal and unzip it with :-unzip /Downloads/ngrok-stable-linux-amd64.zip
3. open the localhost and run your app in any port in another tab
4. Run ./ngrok http 8000
5. Copy the link provided by the ngrok in Forwarding and run it in your browser


```


