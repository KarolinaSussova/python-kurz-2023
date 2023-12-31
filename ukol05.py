import statistics

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

prumer = [statistics.mean(teplota) for teplota in teploty]
rano = [teplota[0] for teplota in teploty]
noc = [teplota[3] for teplota in teploty]
poledne_a_noc = [[teplota[1], teplota[3]] for teplota in teploty]

print(prumer)
print(rano)
print(noc)
print(poledne_a_noc)


# bonus 
teploty = [
    ["pondělí", 2.1, 5.2, 6.1, -0.1],
    ["úterý", 2.2, 4.8, 5.6, -1.0],
    ["středa", 3.3, 6.5, 5.9, 1.2],
    ["čtvrtek", 2.9, 5.6, 6.0, 0.0],
    ["pátek", 2.0, 4.6, 5.5, -1.2],
    ["sobota", 1.0, 3.2, 2.1, -2.0],
    ["neděle", 0.4, 2.7, 1.3, -2.8]
]

prumerna_teplota = {den[0]: statistics.mean(den[1:]) for den in teploty}
print(prumerna_teplota)