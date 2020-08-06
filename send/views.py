from django.shortcuts import render
from django.core.mail import send_mail


def index(request):
    send_mail(
        'Hello',
        'Привет Настя, как дела?',
        'hvoschov.kirill@gmail.com',
        ['tefema8244@mail2paste.com', 'hvoschov.kirill@yandex.ru', 'cpqwi@yandex.ru'],
        fail_silently=False,
    )
    return render(request, 'send/index.html')
