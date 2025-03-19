from flask import Flask, request, render_template
import requests

app = Flask(__name__)

API_KEY = "b49d0b7949d148c38d34c2739761daeb"  # Replace with your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            params = {"q": city, "appid": API_KEY, "units": "metric"}
            response = requests.get(BASE_URL, params=params)
            if response.status_code == 200:
                weather_data = response.json()
            else:
                weather_data = {"error": "City not found"}

    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
