import re, requests
import orodja

STEVILO_STRANI = 5

def html(stran):
    return f'https://www.chessgames.com/perl/chess.pl?page={stran}&playercomp=either&year=1980&yearcomp=ge&moves=15&movescomp=le&result=notdraw'

def nalozi_stran(url):
    print(f'Nalagam {url}...')
    headers = {'Accept-Language': 'de-at;it-it;en-us'}
    odziv = requests.get(url, headers=headers)
    return odziv.text


vzorec = (
    r'<tr bgcolor=#[A-Z]{6}>\n'
    r'<td><font face=.verdana,arial,helvetica. size=-1>'
    r'\d{1,5}'
    r'\.&nbsp;'
    r'<a href="/perl/chessgame\?gid=\d{7}">(?P<igralca>.+?)</a></font></td>\n'
    r'<td valign=TOP NOWRAP>'
    r'.*' #nekateri imajo eno ali dve ikonici, to se vse preskoci
    r'</td>'
    r'<td align=RIGHT NOWRAP>'
    r'<font face=.verdana,arial,helvetica. size=-1>(?P<izid>\d[-]\d)</font></td>'
    r'<td align=RIGHT>'
    r'<font face=.verdana,arial,helvetica. size=-1>(?P<stevilo_potez>\d{1,2})</font></td>'
    r'<td align=RIGHT>'
    r'<font face=.verdana,arial,helvetica. size=-1>(?P<leto>\d{4})</font></td>'
    r'<td><font face=.verdana,arial,helvetica. size=-1>'
    r'<font size=-2>(?P<kraj>.+)</font></font></td>'
    r'<td><font face=.verdana,arial,helvetica. size=-1>'
    r'<font size=-2>'
    r'<a href="/perl/chessopening\?eco=...">(?P<odprtje_stevilka>.{3})</a>'
    r'(?P<odprtje>.+?)</font></font></td></tr>\n'
)


for stran in range(STEVILO_STRANI):
    url = html(stran + 1)
    vsebina = nalozi_stran(url)

    with open(f'datoteke_s_podatki/kratke_igra_saha_stran_{stran}.html', 'w') as f:
        f.write(vsebina)

    with open(f'datoteke_s_podatki/kratke_igra_saha_stran_{stran}.html') as f:
        vsebina = f.read()
        stevec = 0
        print('Berem html ...')
        # print(vsebina)
        for zadetek in re.finditer(vzorec, vsebina):
            stevec += 1
            # print('Iščem vzorec')
            # print(zadetek.groupdict())
        print('Na tej strani sem vzel podatke', stevec, 'iger')