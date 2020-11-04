import re
import orodja




def poisci_indeksa_igralcev(indeks):
    
    with open(f'datoteke_igre/{indeks}.html') as f:
        vsebina = f.read()

    vzorec = (
        r'<b><a href="/perl/chessplayer\?pid=(?P<prvi_id>\d{5,7})">.+</a></b>\n'
        r'<font color="#333333">vs</font>\n'
        r'<b><a href="/perl/chessplayer\?pid=(?P<drugi_id>\d{5,7})">.+</a></b>'
    )

    for zadetek in re.finditer(vzorec, vsebina):
        return zadetek.groupdict()