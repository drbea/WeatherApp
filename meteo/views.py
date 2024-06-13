from django.shortcuts import render
from django.conf import settings
import requests

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST.get('city', 'Paris')  # Récupérer la ville à partir des données POST
        api_key = settings.OPENWEATHERMAP_API_KEY
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        weather_data = response.json()
        
        # Pour le débogage en Python
        print(weather_data)
        
        context = {
            'city': city,
            'weather_data': weather_data,
        }
        
        return render(request, 'meteo/index.html', context)
    
    # Si la méthode n'est pas POST (par exemple, lors de l'accès initial à la page)
    return render(request, 'meteo/index.html')


