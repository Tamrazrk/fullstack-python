def get_full_name(first_name, last_name, middle_name=""):
    return f"{first_name} {middle_name+' ' if middle_name else ''}{last_name}"


print(get_full_name(first_name="john", middle_name="hooker", last_name="lee"))
print(get_full_name(first_name="bruce", last_name="lee"))
