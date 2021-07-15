from django.shortcuts import render
from django.http import HttpResponse
import random

def generator(request):
    return render(request, 'generator/home.html', {})

def about(request):
    return render(request, 'generator/about.html', {})

def show(request):
    if request.method == 'GET':
        lowers = 'abcdefghijklmnopqrstuvwxyz'
        uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        numbers = '0123456789'
        symbols = '!@#$%^&*()'

        is_lower = request.GET.get('lowercase')
        is_upper = request.GET.get('uppercase')
        is_numbers = request.GET.get('numbers')
        is_symbols = request.GET.get('symbols')
        length = int(request.GET.get('length'))

        bag_of_chars = []

        if is_lower:
            bag_of_chars.extend(list(lowers))

        if is_upper:
            bag_of_chars.extend(list(uppers))

        if is_numbers:
            bag_of_chars.extend(list(numbers))

        if is_symbols:
            bag_of_chars.extend(list(symbols))

        if bag_of_chars == []:
            return render(request, 'generator/home.html', {'Error': 'Please select at least one option.'})

        the_password = ''
        for _ in range(length):
            the_password += random.choice(bag_of_chars)
        
        

        return render(request, 'generator/show.html', {'the_password': the_password})

