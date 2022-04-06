from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

def index(request):
    url=f'https://restcountries.com/v2/all'
    result = requests.get(url)
    data= result.json()
    data1={
        'cd':data
    }
    return render(request,'home.html',data1)
    
