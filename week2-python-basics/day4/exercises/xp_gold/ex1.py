def get_age(year, month, day):
    current_year = 2023
    current_month = 8
    current_day = 15

    age = current_year - year

    if current_month < month or (current_month == month and current_day < day):
        age -= 1

    return age


def can_retire(gender, date_of_birth):
    year, month, day = list(map(int, date_of_birth.split("/")))
    age = get_age(year, month, day)

    if gender == "m" and age >= 67 or gender == "f" and age >= 62:
        return True


def main():
    gender = input("input gerder (f)email or (m)ale: ")
    date_of_birth = input("input date of birth in format yyyy/mm/dd: ")
    if can_retire(gender, date_of_birth):
        print("You can retire")
    else:
        print("You can not retire yet")


if __name__ == "__main__":
    main()
