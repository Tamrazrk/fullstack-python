import random


def get_random_temp(season):
    lower, upper = -10, 40
    if season == "winter":
        upper = 16
    elif season == "autumn":
        lower, upper = 10, 30
    elif season == "summer":
        lower = 20
    elif season == "spring":
        lower, upper = 3, 20

    return round(lower + random.random() * (upper - lower), 1)


def main():
    month = int(input("input number of month (number between 1 and 12): "))
    if 3 <= month < 6:
        season = "spring"
    elif 6 <= month < 9:
        season = "summer"
    elif 9 <= month < 12:
        season = "autumn"
    else:
        season = "winter"

    temp = get_random_temp(season)
    print(f"The temperature right now is {temp} degrees Celsius.")

    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif 0 <= temp < 16:
        print("Quite chilly! Don’t forget your coat")
    elif 16 <= temp < 24:
        print("Enjoy the mild weather today! A light jacket should be perfect.")
    elif 24 <= temp < 32:
        print(
            "It's a comfortably warm day! Make sure to stay hydrated and wear something light."
        )
    else:
        print(
            "It's quite hot out there! Stay in the shade, wear sunscreen, and keep yourself cool."
        )


if __name__ == "__main__":
    main()
