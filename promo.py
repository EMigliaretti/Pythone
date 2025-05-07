# Esercizio proposto e risolto in riunione

# Programma_promo

# Un negozio di animali domestici vuole fare uno sconto ai clienti
# che acquistano un animale (o più) e almeno cinque altri articoli.
# Lo sconto è il 20% del costo degli articoli,
# mentre gli animali sono esclusi.

def main():
    prezzi = []
    animale = []
    riga = input("Passami il prezzo pieno e Y/N se animale: ")
    while riga != "-1":
        dati = riga.split(" ")
        prezzi.append(float(dati[0]))
        animale.append(dati[1] == 'Y')
        riga = input("Passami il prezzo pieno e Y/N se animale: ")
    sconto = discount(prezzi, animale, len(prezzi))
    print(sconto)

def discount(prices, isPet, nItems):
#-------------------------------
# Verifica se c'è almeno un animale
    has_pet = any(isPet)
    # Conta il numero di articoli che non sono animali
    non_pet_items = sum(1 for item in isPet if not item)
    # Se c'è almeno un animale  e almeno 5 altri articoli, applica lo sconto
    if has_pet and non_pet_items >= 5:
        # Calcola la somma dei prezzi degli articoli che non sono animali
        non_pet_total = sum(prices[i] for i in range(nItems) if not isPet[i])
        # Applica lo sconto del 20%
        return non_pet_total * 0.2
    else:
        # Nessuno sconto applicabile
        return 0.0
#-------------------------------
main()

