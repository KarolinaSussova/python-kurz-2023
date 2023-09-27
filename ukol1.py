jmeno = 'Karolína'
email = jmeno + '@czechitas.cz'
print(email)

# bonus
# 1. a 2. velká písmenka a malá písmenka
jmeno_a_prijmeni = input('Zde napiš tvé jméno a příjmení: ')
print(jmeno_a_prijmeni.upper())
print(jmeno_a_prijmeni.lower())

# 3. první velké
krestni = input('Křestní jméno: ')
prijmeni = input('Příjmení: ')
print(krestni[0].upper() + krestni[1:].lower() + ' ' + prijmeni[0].upper() + prijmeni[1:].lower())

# 4. inicály
krestni = input('Křestní jméno: ')
prijmeni = input('Příjmení: ')
print(krestni[0].upper() + '.' + prijmeni[0].upper() + '.')

# 5. zkrácení
krestni = input('Křestní jméno: ')
prijmeni = input('Příjmení: ')
if len(krestni) > 5:
    print(krestni[0].upper() + '.' + prijmeni[0].upper() + prijmeni[1:].lower())
else:
    print(krestni[0].upper() + krestni[1:].lower() + ' ' + prijmeni[0].upper() + prijmeni[1:].lower())