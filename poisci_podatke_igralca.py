import re
import orodja

def poisci_podatke_igralca(indeks):

    vzorec = (
        r'<font size=-2>\(born .*(?P<letnica_rojstva>\d{4}).*\) (?P<drzava_rojstva>.*)</font>'
        r'</font></td>\n'
        r'<td background="/chessimages/chessgamesbio\.gif" width=212 align=RIGHT>'
    )

    celoten_html = orodja.nalozi_stran(f'https://www.chessgames.com/perl/chessplayer?pid={indeks}')

    for zadetek in re.finditer(vzorec, celoten_html):
        return zadetek.groupdict()

    return {'letnica_rojstva': None, 'drzava_rojstva': None}