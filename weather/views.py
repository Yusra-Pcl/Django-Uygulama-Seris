import requests
from django.shortcuts import render

def index(request):
    # Bu anahtar senin için özel, tırnakları bozmadan yapıştır:
    api_key = 'b6907d289e10d714a6e88b30761fae22'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'
    
    city = 'Ankara'
    
    if request.method == 'POST':
        city = request.POST.get('city')

    # İnternetten veriyi çek ve terminale yazdır (Buraya bakacağız!)
    response = requests.get(url.format(city, api_key)).json()
    print("--- TERMİNAL ÇIKTISI BAŞLADI ---")
    print(response)
    print("--- TERMİNAL ÇIKTISI BİTTİ ---")

    if response.get('main'):
        weather_data = {
            'city': city,
            'temperature': response['main']['temp'],
            'description': response['weather'][0]['description'],
            'icon': response['weather'][0]['icon'],
        }
    else:
        weather_data = None

    return render(request, 'weather/index.html', {'weather': weather_data})