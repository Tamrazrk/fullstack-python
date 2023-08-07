import matplotlib.pyplot as plt
import pytz
from datetime import datetime, timedelta
import pyowm


owm = pyowm.OWM("c619d6bc7639da6f5aa906c052ced087")
city_name = "London"
country_code = "GB"
time_zone = "Europe/London"

weather_manager = owm.weather_manager()
forecast = weather_manager.forecast_at_place(
    f"{city_name},{country_code}", interval="3h", limit=20
).forecast


def init_plot():
    plt.figure(figsize=(10, 6))
    plt.xlabel("Date")
    plt.ylabel("Humidity (%)")
    plt.title(f"Humidity Forecast - {city_name}, {country_code}")
    plt.grid(axis="y")


def plot_humidity(dates, humidity_values):
    plt.bar(dates, humidity_values, width=0.6, align="center", color="skyblue")


def write_humidity_on_bar_chart(dates, humidity_values):
    for i, value in enumerate(humidity_values):
        plt.text(i, value + 1, f"{value}%", ha="center", fontsize=10)


def plot_humidity_forecast():
    forecast_data = forecast.weathers[::8]

    dates = []
    humidity_values = []

    for weather in forecast_data:
        forecast_time = weather.reference_time(timeformat="iso")
        local_time = datetime.fromisoformat(
            forecast_time.replace("Z", "+00:00")
        ).astimezone(pytz.timezone(time_zone))
        date = local_time.strftime("%Y-%m-%d %H:%M:%S")
        dates.append(date)
        humidity_values.append(weather.humidity)

    init_plot()
    plot_humidity(dates, humidity_values)
    write_humidity_on_bar_chart(dates, humidity_values)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


plot_humidity_forecast()
