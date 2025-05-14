# atp
# estrarre i dati relativi alla classifica (ranking) dei primi 100 tennisti

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

url = "https://live-tennis.eu/it/classifica-atp-live"
# =========================================================================
s = Service(r"/Program Files/Python/Python313/chromedriver.exe")
# =========================================================================

driver = webdriver.Chrome(service=s)
driver.get(url)

rows = driver.find_elements(By.TAG_NAME, "tr")

# Lista per salvare i dati
dati_classifica = []

for row in rows:
    celle = row.find_elements(By.TAG_NAME, "td")

    # Ignora le righe che non hanno almeno 7 celle significative
    if len(celle) < 7:
        continue

    testo_posizione = celle[0].text.strip()
    if not testo_posizione or not testo_posizione.split()[0].isdigit():
        continue

    posizione = testo_posizione.split()[0]
    nome = celle[3].text.strip()
    nazione = celle[5].text.strip()
    eta = celle[4].text.strip()
    punti = celle[6].text.strip()

    dati_classifica.append({
        "Posizione": int(posizione),
        "Nome": nome,
        "Nazione": nazione,
        "Età": int(eta),
        "Punti": int(punti.replace(',', ''))
    })

    if posizione == "100":
        break

driver.quit()

# Crea DataFrame pandas
df = pd.DataFrame(dati_classifica)

# Mostra la tabella in modo ordinato
pd.set_option("display.max_rows", None)  # Mostra tutte le righe
print(df.to_string(index=False))


# Opzioni per l'output

# df.to_csv("classifica_atp.csv", index=False, encoding="utf-8")
# df.to_excel("classifica_atp.xlsx", index=False)



