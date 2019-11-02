import requests, json

api_key = "dede88a93c0742b8843113317190708"

base_url = "http://api.apixu.com/v1/current.json?"

while (True):
    city_name = input("Enter the location : ")
    complete_url = base_url + "key=" + api_key + "&q=" + city_name

    response = requests.get(complete_url)

    x = response.json()
    country = x['location']['country']
    city = x['location']['name']
    condition = x['current']['condition']['text']
    temperature_c = x['current']['temp_c']
    humidity = x['current']['humidity']
    wind_mph = x['current']['wind_mph']

    print(
        """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(
            condition, city, temperature_c, humidity, wind_mph))

#     print("weather in {}".format(city_name)+ "is {}".format(x['current']['']))
