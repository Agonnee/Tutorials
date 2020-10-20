from tkinter import *
from PIL import ImageTk,Image
import requests
import json

#Learning to use an API request

# API REMOVED Prior to putting on Github

root = Tk()
root.title("Learn to Code with Agonnee")
root.geometry("500x100")

# Create Lookup func
def ziplookup():
    #zip.get()
    #ziplabel = Label(root, text=zip.get())
    #ziplabel.grid(row=1, column=0, columnspan=2)

    try:
        api_request = requests.get(
            "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+ zip.get() +"&distance=2&API_KEY=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        state = api[0]['StateCode']
        aqi = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == "Good":
            weather_color = "#0C0"
        elif category == "Moderate":
            weather_color = "#FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#ff9900"
        elif category == "Unhealthy":
            weather_color = "#FF0000"
        elif category == "Very Unhealthy":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "#660000"

        root.configure(background=weather_color)

        mylabel = Label(root, text=city + "'s Air Quality: " + str(aqi) + " " + category, font=("Comic Sans MS", 12), background=weather_color)
        mylabel.grid(row=1, column=0, columnspan=2)
    except Exception as e:
        api = "Error..."





zip = Entry(root)
zip.grid(row=0, column=0, sticky=W+E+N+S)
subbtn = Button(root, text="Zip Code Lookup", command=ziplookup)
subbtn.grid(row=0, column=1, sticky=W+E+N+S)



root.mainloop()
