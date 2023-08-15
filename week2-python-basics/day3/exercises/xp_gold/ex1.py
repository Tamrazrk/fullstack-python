birthdays = {
    "Nick": "1974/07/14",
    "Alex": "1996/06/20",
    "Tamar": "1994/07/20",
    "Fredrin": "2006/01/01",
    "Karina": "2017/03/08",
}

print(
    "Welcome to Birthday checker.\n"
    "You can look up the birthdays of the people in the list!"
)

name = input("input person's name: ")
birthday = birthdays.get(name)
if birthday:
    print(f"{name} is born in {birthday}")
