from pyowm.owm import OWM

owm = OWM("c619d6bc7639da6f5aa906c052ced087")
weather_manager = owm.weather_manager()
airpollution_manager = owm.airpollution_manager()


def print_weather_data(weather):
    current_status = weather.detailed_status
    sunrise_time = weather.sunrise_time("iso")
    sunset_time = weather.sunset_time("iso")
    wind_info = weather.wind()

    print(
        f"\tWeather Status: {current_status}\n"
        f"\tWind info: {wind_info['speed']} m/h, {wind_info['deg']} degree\n"
        f"\tSunrise time: {sunrise_time}\n"
        f"\tSunset time: {sunset_time}"
    )


def print_city_weather_info(city_name=None, city_id=None):
    """if city_id is not None then it is used to fetch city weather info,
    otherwise city_name is used"""
    if city_id:
        observation = weather_manager.weather_at_id(city_id)
    else:
        observation = weather_manager.weather_at_place(city_name)

    location = observation.location
    city_name = f"{location.name}, {location.country}"
    print(f"Today's weather info in {city_name}.")
    print_weather_data(weather=observation.weather)


if __name__ == "__main__":
    print_city_weather_info(city_name="Tel Aviv")
    print()
    print_city_weather_info(city_id=5391959)
