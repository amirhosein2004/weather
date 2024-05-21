from django.shortcuts import render
# import json to load json data to python dictionary 
import json
# urllib.request to make a request to api 
import urllib.request
from django.views import View

class BaseWeatherView(View):
    api_key = 'your_api_key_here'

    def get_weather_data(self, city):
        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q='
            + city + '&appid=' + self.api_key).read()
        list_of_data = json.loads(source)
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                          + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
        return data

    def get(self, request):
        return render(request, "main/index.html", {})

    def post(self, request):
        city = request.POST.get('city')
        data = self.get_weather_data(city)
        print(data)
        return render(request, "main/index.html", data)

# def index(request):
#     if request.method == 'POST':
#         city = request.POST['city']
#         ''' api key might be expired use your own api_key
#             place api_key in place of appid ="your_api_key_here "  '''
#
#         # source contain JSON data from API
#
#         source = urllib.request.urlopen(
#             'http://api.openweathermap.org/data/2.5/weather?q ='
#             + city + '&appid = 66d2d2cdbf52a29baf09c18cf2116b3a').read()
#
#         # converting JSON data to a dictionary
#         list_of_data = json.loads(source)
#
#         # data for variable list_of_data
#         data = {
#             "country_code": str(list_of_data['sys']['country']),
#             "coordinate": str(list_of_data['coord']['lon']) + ' '
#                           + str(list_of_data['coord']['lat']),
#             "temp": str(list_of_data['main']['temp']) + 'k',
#             "pressure": str(list_of_data['main']['pressure']),
#             "humidity": str(list_of_data['main']['humidity']),
#         }
#         print(data)
#     else:
#         data = {}
#     return render(request, "main/index.html", data)