class Cat:
    def __init__(self, cat_name, cat_age):
        """creates new cat instance with name and age"""
        self.name = cat_name
        self.age = cat_age


def find_oldest(cats):
    """returns oldest cat from cats list"""
    oldest_cat = cats[0]
    for cat in cats[1:]:
        if cat.age > oldest_cat.age:
            oldest_cat = cat
    return oldest_cat


cat1 = Cat("cat1", 1)
cat2 = Cat("cat2", 15)
cat3 = Cat("cat3", 7)

oldest_cat = find_oldest([cat1, cat2, cat3])

print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")
