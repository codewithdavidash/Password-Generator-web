import random
from django.shortcuts import render


def index(request):
    lower_chars = 'abcdefghijklmnopqrstuvwxyz'
    upper_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = "1234567890"
    symbols = '~!@#$%^&*_+-='
    all_chars = lower_chars + upper_chars + numbers + symbols
    char_length = 8
    password = "".join(random.sample(all_chars, char_length))
    print(f"Generated Password: {password}")
    return render(request, 'index.html', {
        'password': password
    })
