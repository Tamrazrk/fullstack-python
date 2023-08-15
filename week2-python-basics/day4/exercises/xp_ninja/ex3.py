def box_printer(*args):
    max_len = max(list(map(lambda s: len(s), args)))
    print("*" * (max_len + 4))
    for s in args:
        print(f"* {s}{' '*(max_len-len(s))} *")
    print("*" * (max_len + 4))


if __name__ == "__main__":
    box_printer("hello", "world", "realylogword", "in", "a", "frame")
