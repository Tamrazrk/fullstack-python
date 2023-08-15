choice = input("select (e)ncode or (d)ecode: ")

if choice not in "ed":
    print("wrong choice!")
    exit()

message = input("input a message: ")
shift = int(input("input a shift: "))

if choice == "d":
    shift = -shift

print(
    f"{'decoded' if choice == 'd' else 'encoded'} message: "
    f"{''.join(chr(ord(letter) + shift) for letter in message)}"
)
