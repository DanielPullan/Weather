import requests
import json
from key import apikey

## Weather App
## Get weather from Dark Sky, change webpage depending on the result
## Night? Dark background.
## Rain? Rain animation
## Wind? Text aligns the direction the wind comes. 
## Lots of wind? Text g o e s  l i k e  t h i s
## Cloud? Grey header top
## No cloud during day? Blue header top
## Moon phase shows during night time
## Sun shows during day time

# Location currently set to Uxbridge in London, UK
latitude = "51.545151"
longitude = "-0.481630"
location = "Uxbridge"

# Make API call to dark sky
r = requests.get("https://api.darksky.net/forecast/"+apikey+"/"+latitude+","+longitude+"?exclude=currently,minutely,hourly,flags&units=uk2")

# Load data into something we can play with
data = json.loads(r.text)

# Write data to json file for safekeeping
f = open("data.json", 'w')
f.write(str(data))
f.close()

# Will always have data defined
weather = data['daily']['data'][0]['icon']
tempMax = str(data['daily']['data'][0]['temperatureMax'])
tempLow = str(data['daily']['data'][0]['temperatureLow'])
wind = str(data['daily']['data'][0]['windSpeed'])

# Sometimes might not have data defined
precip = data['daily']['data'][0]['precipType']

# Creating the weather config file
webpage = ("""
var weather = 	"%s";
var tempMax = 	"%s";
var tempLow = 	"%s";
var wind = 		"%s";

document.getElementById('weather').innerHTML = weather;
document.getElementById('tempMax').innerHTML = tempMax;
document.getElementById('tempLow').innerHTML = tempLow;
document.getElementById('wind').innerHTML = wind;	
"""% (weather, tempMax, tempLow, wind))

f = open('weather.js', 'w')

f.write(webpage)

f.close()


# Start printing our hard-earned data
print("The current weather in " + location +" is " + weather + " with a low of " + tempLow + " and a high of " + tempMax + 
	  ". The wind speed is " + wind + ".")