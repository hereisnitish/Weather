from django.shortcuts import render
from django.http import JsonResponse
import urllib.request
import json
from django.shortcuts import render
# Create your views here.




def index(request):

    if request.method == 'POST':
        country = request.POST['country']
        state = request.POST['state']
        city = request.POST['city']

        source = urllib.request.urlopen('http://api.weatherstack.com/current?access_key=499926bcaf71ac88510480a752017b9b&query={},{},{}'.format(city, state, country)).read()

        #source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q={},{}&units=metric&appid=09051d463a38f5480cf66f15c3d24ae1'.format(city, state, country)).read()
        list_of_data = json.loads(source)
        print(list_of_data)

        data = {
            "country_code": str(list_of_data['location']['country']),
            "city_name": str(list_of_data['location']['name']),
            "coordinate": str(list_of_data['location']['lon']) + ', '
            + str(list_of_data['location']['lat']),

            "temp": str(list_of_data['current']['temperature']) + ' °C',
            "pressure": str(list_of_data['current']['pressure']),
            "humidity": str(list_of_data['current']['humidity']),
            #'main': str(list_of_data['weather'][0]['main']),
            #'description': str(list_of_data['weather'][0]['description']),
            #'icon': list_of_data['weather'][0]['icon'],
        }
        print(data)
        return JsonResponse(data)
    else:
        data = {}

    return render(request, "index.html", data)
