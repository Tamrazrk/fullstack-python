# 4.1
items = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}

print(
    f"items info: {', '.join(f'{item} costs ${cost}' for item, cost in items.items())}."
)

# 4.2
items = {
    "banana": {"price": 4, "stock": 10},
    "apple": {"price": 2, "stock": 5},
    "orange": {"price": 1.5, "stock": 24},
    "pear": {"price": 3, "stock": 1},
}

total_cost = sum(list(map(lambda item: item["price"] * item["stock"], items.values())))
print(f"total cost: {total_cost}")
