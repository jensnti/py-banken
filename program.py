pin = 1234

userPin = int(input("Skriv in din pinkod: "))

if pin != userPin:
    exit()

balance = 0.0
menu = 0
# menu 1 insättning
# menu 2 uttag
# menu 3 avsluta
while menu != 3:
    print("Ditt saldo är: ", balance)
    menu = int(input("Skriv ditt val[1, 2, 3]: "))
    if menu == 1:
        balance = balance + float(input("Gör en instättning: "))
    elif menu == 2:
        print("uttag")
    else:
        print("Fel eller avslut")