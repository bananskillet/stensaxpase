import random

print("Välkommen till spelet sten-sax-påse!")

while True:
    anv_val = input("Skriv sten, sax eller påse och tryck på enter:").lower()

    dat_val = random.choice(["sten", "sax", "påse"])
    print(f"Du valde {anv_val} : datorn valde {dat_val}.")

    if anv_val == dat_val:
        print("Ni valde samma, Lika!")
    elif (
        (anv_val == "påse" and dat_val == "sten") or
        (anv_val == "sax" and dat_val == "påse") or
        (anv_val == "sten" and dat_val == "sax")
    ):
        print("Du vann!")
    else:
        print("Datorn vann!")

print("Tack för att du spelade!")