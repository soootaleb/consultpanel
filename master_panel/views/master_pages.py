from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as lin, logout as lout # To avoid ambigous function name
from public_site import forms
from django.contrib import messages

def index(request):
    return render(request, 'master_pages_index.html')

def todo(request):
    return render(request, 'master_pages_todo.html')