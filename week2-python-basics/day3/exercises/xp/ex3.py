# task 2
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": ["blue"],
        "Spain": ["red"],
        "US": ["pink", "green"],
    },
}

# task 3
brand["number_stores"] = 2

# task 4 - ambiguous

# task 5
brand["country_creation"] = "Spain"

# task 6
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# task 7
brand.pop("creation_date")

# task 8
print(f'last international competitor: {brand["international_competitors"][-1]}')

# task 9
print(f"major clothes colors in the US: {brand['major_color']['US']}")

# task 10
print(len(brand))

# task 11
print(list(brand.keys()))

# task 11
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000,
}

# task 12
brand.update(more_on_zara)

# task 13
print(brand["number_stores"])
