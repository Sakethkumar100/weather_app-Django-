import requests
from django.shortcuts import render

def weather_view(request):
    city = request.POST.get("city", "Hyderabad")  # Default city if nothing entered
    api_key = "467fa89b03484f8d2633cb621dfb6e64"
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    weather_data = {}
    error_message = None

    if request.method == "POST":
        try:
            response = requests.get(base_url, params={
                "q": city,
                "appid": api_key,
                "units": "metric"
            })

            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    "city": data["name"],
                    "temperature": data["main"]["temp"],
                    "description": data["weather"][0]["description"].title(),
                    "icon": data["weather"][0]["icon"]
                }
            else:
                error_message = f"City '{city}' not found. Try another."

        except Exception as e:
            error_message = str(e)

    return render(request, "main/index.html", {
        "weather_data": weather_data,
        "error_message": error_message
    })
