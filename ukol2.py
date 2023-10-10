sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

soucastka = input('zadejte kód součástky: ')
pocet = ('zadejte požadovan počet: ')

for key in sklad:
    if soucastka not in key:
        print('Tato součástka bohužel neí na skladě')


# morseovka
morse_code = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-",
}



text = input('zadej slovo: ')

for pismeno in text:
    if pismeno in morse_code:
        print(morse_code[pismeno], end="/")
    if pismeno == " ":
        print('/', end="")



# staty a regiony řešení

selected_region = input("Zadej region: ")

for stat in staty:
    if selected_region == stat["region"]:
        print(stat["name"])  

regiony = []
for stat in staty:
    if stat["region"] not in regiony:
        regiony.append(stat["region"])

if selected_region not in regiony:
    print("neznámý region")
