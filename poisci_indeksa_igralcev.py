import re
import orodja


def poisci_indeksa_igralcev(indeks):

    vzorec = (
        r'<b><a href="/perl/chessplayer\?pid=(?P<prvi_id>\d{5,7})">.+</a></b>\n'
        r'<font color="#333333">vs</font>\n'
        r'<b><a href="/perl/chessplayer\?pid=(?P<drugi_id>\d{5,7})">.+</a></b>'
    )

    with open(f'html_datoteke_igre/{indeks}.html') as f:
        vsebina = f.read()

    for zadetek in re.finditer(vzorec, vsebina):
        return zadetek.groupdict()

    return {'prvi_id': None, 'drugi_id': None}