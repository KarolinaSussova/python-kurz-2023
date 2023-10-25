import math

def verify_tel_number(tel_number):
    if len(tel_number) == 9:
        return True
    elif len(tel_number) == 13:
        if tel_number[0:4] == '+420':
            return True
        else: 
            return False
    else:
        return False
    
def price_of_message(message):
    return math.ceil((len(message)/ 180)) * 3
    

    
tel_number = input('Zadej telefonní číslo: ')


if verify_tel_number(tel_number) == False:
    print('Špatný formát čísla')
else:
    message = input('Zadej svou zprávu: ')
    print(f'Cena vaší zprávy je {price_of_message(message)} Kč')