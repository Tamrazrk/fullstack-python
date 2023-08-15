def parse_money(money_str):
    return float("".join(c for c in money_str if c.isdigit()))


def find_answer(items_purchase, wallet):
    ans = list(
        sorted(
            [
                item
                for item, price in items_purchase.items()
                if parse_money(price) <= parse_money(wallet)
            ]
        )
    )
    print(ans if len(ans) else "Nothing")


if __name__ == "__main__":
    # test 1
    items_purchase = {
        "Water": "$1",
        "Bread": "$3",
        "TV": "$1,000",
        "Fertilizer": "$20",
    }
    wallet = "$300"
    find_answer(items_purchase, wallet)

    # test 2
    items_purchase = {
        "Apple": "$4",
        "Honey": "$3",
        "Fan": "$14",
        "Bananas": "$4",
        "Pan": "$100",
        "Spoon": "$2",
    }
    wallet = "$100"
    find_answer(items_purchase, wallet)

    # test 3
    items_purchase = {
        "Phone": "$999",
        "Speakers": "$300",
        "Laptop": "$5,000",
        "PC": "$1200",
    }
    wallet = "$1"
    find_answer(items_purchase, wallet)
