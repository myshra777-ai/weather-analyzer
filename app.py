from flask import Flask, jsonify
import os
import requests

app = Flask(__name__)

# Load environment variables
API_KEY = os.getenv("API_KEY")
DEFAULT_CITY = os.getenv("DEFAULT_CITY", "Indore")
LOG_FILE = os.getenv("LOG_FILE", "/output/weather_log.txt")
DATA_FILE = os.getenv("DATA_FILE", "/output/weather_data.csv")

def get_weather_data():
    if not API_KEY:
        print("❌ API_KEY is missing")
        return None

    url = f"http://api.openweathermap.org/data/2.5/weather?q={DEFAULT_CITY}&appid={API_KEY}&units=metric"
    print(f"🌐 Requesting: {url}")

    try:
        response = requests.get(url)
        data = response.json()
        print(f"📦 Response: {data}")

        if response.status_code != 200 or "main" not in data:
            print("⚠️ Invalid response or missing 'main'")
            return None

        temperature = data["main"]["temp"]
        city = data.get("name", DEFAULT_CITY)

        # Write to log file
        try:
            with open(LOG_FILE, "a") as log:
                log.write(f"{city},{temperature}\n")
            print(f"📝 Logged to {LOG_FILE}")
        except Exception as log_err:
            print(f"⚠️ Failed to write log: {log_err}")

        # Write to CSV file
        try:
            with open(DATA_FILE, "a") as csv:
                csv.write(f"{city},{temperature}\n")
            print(f"📊 Saved to {DATA_FILE}")
        except Exception as csv_err:
            print(f"⚠️ Failed to write CSV: {csv_err}")

        return city, temperature

    except Exception as e:
        print(f"❌ Error fetching weather data: {e}")
        return None

@app.route("/")
def home():
    return "✅ Weather Analyzer is live!"

@app.route("/weather")
def weather():
    result = get_weather_data()
    if result is None:
        return jsonify({"error": "Weather data not available"}), 500

    city, temp = result
    return jsonify({"city": city, "temperature": temp})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
