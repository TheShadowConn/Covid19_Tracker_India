from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.

def home(request):
    import requests

    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring={"country":"India"}

   

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "fd2756895emsh0f32df097cb0b73p152af3jsnfbf889f5a70e"
        }

    response = requests.request("GET", url, headers=headers,params=querystring).json()

    data=response['response']

    d=data[0]


    print(d)

    context={
        'recovered':d['cases']['recovered'],
        'infected':d['cases']['active'],
        'death':d['deaths']['total'],
        'total':d['tests']['total']
    }

    
    return render(request,'index.html',context)
