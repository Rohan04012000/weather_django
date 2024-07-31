from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    API_KEY = open("API_KEY", "r").read() #Read the API KEY
    current_base_weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

    #Check if it's a POSt or GET request.
    if request.method == "POST":
        city1  = request.POST['city1']  #We have to have City1.
        city2 = request.POST.get('city2', None) # Try to get city2, if it does not exist, it is also fine.

        #Out-source the functionality of weather api to function fetch_weather_details().
        weather_data_city1 = fetch_weather_details(city1, API_KEY, current_base_weather_url)

        #Check if there is city2.
        if city2:
            weather_data_city2 = fetch_weather_details(city2, API_KEY, current_base_weather_url)
        else:
            weather_data_city2 = None

        #When there is no record found for the given City name.
        if not weather_data_city1:
            return render(request, "weather_app/index.html")
        if not weather_data_city2:
            weather_data_city2 = None

        #Now create a dictionary to render it.
        context_dict = {
            "weather_data_city1":weather_data_city1,
            "weather_data_city2":weather_data_city2
        }
        return render(request, "weather_app/index.html", context_dict)

    else:
        return render(request, "weather_app/index.html")

def fetch_weather_details(city, api_key, base_weather_url):
    response = requests.get(base_weather_url.format(city, api_key)).json() #Getting the response as Json object.
    #latitude, longitude = response['coord']['lat'], response['coord']['lon']

    #Take the information, and format it into the way, that can easily be passed into the templates.
    if len(response) != 2:
        weather_data = {
            "city":city,
            "temperature":round(response['main']['temp'] - 273.15, 2), #Convert to celcisu from Kelvin and round to 2 decimal points.
            "description":response['weather'][0]['description'],
            "icon":response['weather'][0]['icon']
        } #All this is knowning the Api.
        print("fetched weather_data details = ", weather_data)
        return weather_data
    else:
        return False
