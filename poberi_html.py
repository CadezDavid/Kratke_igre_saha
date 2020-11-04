import re, requests
import orodja

stevilo_strani = 200

def html(stran):
    return f'https://www.chessgames.com/perl/chess.pl?page={stran}&playercomp=either&year=1980&yearcomp=ge&moves=15&movescomp=le&result=notdraw'

for stran in range(stevilo_strani):
    url = html(stran + 1)
    vsebina = orodja.nalozi_stran(url)

    with open(f'datoteke/kratke_igra_saha_stran_{stran}.html', 'w') as f:
        f.write(vsebina)