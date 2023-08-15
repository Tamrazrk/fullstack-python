# task 1 and 2
company_list = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet".split(", ")

# task 3
print(f"there are {len(company_list)} companies in the list")

# task 4
print(sorted(company_list, reverse=True))

# task 5.1
print(
    len([company for company in company_list if "o" in company]),
    "company name contains 'o'",
)

# task 5.2
print(
    len([company for company in company_list if "i" not in company]),
    "company name does not contain 'i'",
)


# task 6.1
duplicated = [
    "Honda",
    "Volkswagen",
    "Toyota",
    "Ford Motor",
    "Honda",
    "Chevrolet",
    "Toyota",
]

single = set(duplicated)

# task 6.2
print(f"companies list: {', '.join(company for company in single)}")
print(f"there are {len(single)} company in the list")

# task 7
print([company[::-1] for company in sorted(single)])
