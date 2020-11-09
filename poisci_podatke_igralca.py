import re
import orodja

def poisci_podatke_igralca(indeks):

    if indeks == None:
        print('Nisem dobil smiselnega indeks ... :(')
        return {'letnica_rojstva': None, 'drzava_rojstva': None} 

    vzorec = (
        r'<font size=-2>\(.*?(?P<letnica_rojstva>\d{4}).*?\)(?P<drzava_rojstva>.*)</font>'
        r'</font></td>\n'
        r'<td background="/chessimages/chessgamesbio\.gif" width=212 align=RIGHT>'
    )

    with open(f'datoteke_igralci/{indeks}.html') as f:
        vsebina = f.read()

    for zadetek in re.finditer(vzorec, vsebina):
        return zadetek.groupdict()

    return {'letnica_rojstva': None, 'drzava_rojstva': None}