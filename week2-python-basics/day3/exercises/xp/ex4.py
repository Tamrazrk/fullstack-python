users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# task 1
disney_users_A = {}
for value, key in enumerate(users):
    disney_users_A[key] = value
print(disney_users_A)

# task 2
disney_users_B = {}
for key, value in enumerate(users):
    disney_users_B[key] = value
print(disney_users_B)

# task 3
disney_users_C = {}
for value, key in enumerate(sorted(users)):
    disney_users_C[key] = value
print(disney_users_C)


# task 4.1
result1 = {}
for value, key in enumerate(filter(lambda x: "i" in x, users)):
    result1[key] = value
print("4.1 result:", result1)

# task 4.2
result2 = {}
for value, key in enumerate(filter(lambda x: x[0].lower() in ("mp"), users)):
    result2[key] = value
print("4.2 result:", result2)
