


vokaler = "aeiouyåaö"
konsonanter = "bcdfghjklmnpqrstvwxz"

# userString = "Hej! Kom in."
userString = input("Skriv en mening: ")
# Hohejoj! Kokomom inon,

newString = ""

for c in userString:
    if konsonanter.find(c.lower()) > -1:
        newString += f"{c}o{c.lower()}"
    else:
        newString += c

print(newString)