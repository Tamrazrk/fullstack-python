family = dict()

n = int(input("input number of family members: "))
for _ in range(n):
    name = input("input member's name: ")
    age = int(input("input members's age: "))
    family[name] = age

total_cost = 0
for name, age in family.items():
    cost = 0
    if 3 <= age <= 12:
        cost = 10
    elif age > 12:
        cost = 15
    total_cost += cost
    print(f"{name} pays: ${cost}")

print(f"family's total cost for movies is: ${total_cost}")
