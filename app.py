from flask import Flask, request, render_template
import requests

app = Flask(__name__)

BASE_URL = "https://restcountries.com/v3.1/name/"

@app.route("/", methods=["GET"])
def home():
    country = request.args.get("country")
    country_data = None

    if country:
        response = requests.get(BASE_URL + country)

        if response.status_code == 200:
            country_info = response.json()[0]  # Get the first match
            country_data = {
                "name": country_info["name"]["common"],
                "capital": country_info.get("capital", ["N/A"])[0],
                "population": country_info.get("population", "N/A"),
                "currency": list(country_info["currencies"].keys())[0] if "currencies" in country_info else "N/A",
                "language": list(country_info["languages"].values())[0] if "languages" in country_info else "N/A",
                "flag": country_info["flags"]["png"] if "flags" in country_info else None
            }
        else:
            country_data = {"error": "Country not found. Please check the name and try again."}

    return render_template("index.html", country=country_data)

if __name__ == "__main__":
    app.run(debug=True)
