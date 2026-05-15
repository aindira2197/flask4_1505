def check_password(password):
    upper = False
    lower = False
    digit = False

    for char in password:
        if char.isupper():
            upper = True

        if char.islower():
            lower = True

        if char.isdigit():
            digit = True

    if len(password) >= 8 and upper and lower and digit:
        return "Kuchli parol"

    return "Kuchsiz parol"

password = input("Parol kiriting: ")

result = check_password(password)

print(result)
