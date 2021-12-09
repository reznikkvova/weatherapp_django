from django.shortcuts import render, redirect
import requests
from .models import City
from .forms import CityForm


def index(request):
    appid = '42c4b391896106b8a34a138b591bc85c'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    cities = City.objects.all()
    all_cities = []

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"],
            'temp_min': res["main"]["temp_min"],
            'temp_max': res["main"]["temp_max"],
            'feels_like': res["main"]["feels_like"]
        }
        all_cities.append(info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)


def del_city(request, city_id):
    City.objects.get(id=city_id).delete()
    return redirect('/')



