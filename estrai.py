# Estrai
# modificare il programma (su PDF) in modo da:
# - non estrarre più il numero di sequenza
# - emettere in ordine: sigla, nome provincia, abitanti, kmq
# - ricalcolare la densità per kmq e confrontarla col valore in tabella
#   segnalando eventuali divergenze

import urllib.request
url = "https://www.comuni-italiani.it//province.html"
response = urllib.request.urlopen(url)
theBytes = response.read()
text = theBytes.decode(encoding="iso-8859-1")

lista = []
import bs4
doc = bs4.BeautifulSoup(text, "html.parser")
elems = doc.find_all("table")
table = elems[3]
for tr in table.contents[2:-2]:
    if type(tr) == bs4.element.Tag:
        tds = tr.contents
        # sequ = int(tds[0].get_text())
        sigl = tds[7].get_text()
        prov = tds[1].get_text()
        resi = int(tds[2].get_text().replace(".", ""))
        kmqd = int(tds[4].get_text().replace(".", ""))
        dens = float(tds[5].get_text().replace(".", "").replace(",", "."))
        dens_n = round(resi / kmqd, 1)
        delta = round(dens - dens_n, 1)
        # print(f"{sigl} {prov} {resi:9d} {kmqd:5d} {dens} {dens_n} {delta}")
        lista.append([sigl, prov, resi, kmqd, dens, dens_n, delta])

import pandas as pd

# Impostazione opzione pd per la visualizzazione estesa
pd.set_option('display.max_rows', None)

df = pd.DataFrame(lista, columns=['Sigla', 'Provincia', 'Resid.', \
'KMq', 'Dens.orig.', 'Dens.nuova', 'Delta'])
print(df)

# Possibilità di salvare il DataFrame su un file CSV
# df.to_csv("province.csv", index=False)


        
    
