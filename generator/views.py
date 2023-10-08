from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    # return the text back to the user
    # we need to format it as a http response
    # render allows us to pass through a template tha enventualy translate to a http response
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
# where we want our random pass to be generated

   

    characters = list('zxcvbnmlkjhgfdsaqwertyuiop')
    #checking if users want special characters
    if request.GET.get('uppercase'):
        characters.extend('ZXCVBNMASDFGHJKLPOIUYTREWQ')

    #Special characters
    if request.GET.get('special characters'):
        characters.extend('~`!@#$%^&*()_+=-<>?/|')

    #numbers
    if request.GET.get('numbers'):
        characters.extend('1234567890')

    length = int(request.GET.get('length', 14))

    the_password = ''
    for x in range(length):
        the_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': the_password})