import re, orodja, poisci_podatke_igralca, poisci_indeksa_igralcev


def shrani_html_igre(indeks):
    url = f'https://www.chessgames.com/perl/chessgame?gid={indeks}'
    orodja.shrani_spletno_stran(url, f'datoteke_igre/{indeks}.html')

def shrani_html_igralcev(indeks):
    indeksa_igralcev = poisci_indeksa_igralcev.poisci_indeksa_igralcev(indeks)
    for igralec in indeksa_igralcev:
        url = f'https://www.chessgames.com/perl/chessplayer?pid={indeksa_igralcev[igralec]}'
        orodja.shrani_spletno_stran(url, f'datoteke_igralci/{indeksa_igralcev[igralec]}.html')


vzorec = (
    r'<tr bgcolor=#[A-Z]{6}>\n'
    r'<td><font face=.verdana,arial,helvetica. size=-1>'
    r'\d{1,5}'
    r'\.&nbsp;'
    r'<a href="/perl/chessgame\?gid=(?P<indeks_igre>\d{7})">(?P<prvi_igralec>.+)vs(?P<drugi_igralec>.+)</a></font></td>\n'
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
    r'<font size=-2>(<.+>)?(?P<kraj>.+)(</a>)?</font></font></td>'
    r'<td><font face=.verdana,arial,helvetica. size=-1>'
    r'<font size=-2>'
    r'<a href="/perl/chessopening\?eco=...">(?P<odprtje_neka_stevilka>.{3})</a>'
    r'(?P<odprtje>.+?)</font></font></td></tr>\n'
)

igre = list()
igralci = list()
seznam_igralcev = list() #Da se ne bodo podvajali, bom v ta seznam shranjeval indekse
stevec = 0

for stran in range(200):
	with open(f'datoteke/kratke_igra_saha_stran_{stran}.html') as f:
		print('Zdej sem v', stran, 'strani.')
		vsebina = f.read()
		for zadetek in re.finditer(vzorec, vsebina):
			podatki_igre = zadetek.groupdict()

			idja_igralcev = poisci_indeksa_igralcev.poisci_indeksa_igralcev(podatki_igre['indeks_igre'])
			podatki_igre.update(idja_igralcev)

			podatki_prvega = poisci_podatke_igralca.poisci_podatke_igralca(idja_igralcev['prvi_id'])
			podatki_drugega = poisci_podatke_igralca.poisci_podatke_igralca(idja_igralcev['drugi_id'])

			podatki_igre = orodja.strip_vse(podatki_igre)

			if idja_igralcev['prvi_id'] not in seznam_igralcev:
				podatki_prvega.update({'id': idja_igralcev['prvi_id'], 'ime': podatki_igre['prvi_igralec']})
				podatki_prvega = orodja.strip_vse(podatki_prvega)
				igralci.append(podatki_prvega)
				seznam_igralcev.append(idja_igralcev['prvi_id'])

			if idja_igralcev['drugi_id'] not in seznam_igralcev:
				podatki_drugega.update({'id': idja_igralcev['drugi_id'], 'ime': podatki_igre['drugi_igralec']})
				podatki_drugega = orodja.strip_vse(podatki_drugega)
				igralci.append(podatki_drugega)
				seznam_igralcev.append(idja_igralcev['drugi_id'])

			igre.append(podatki_igre)

imena_polj_csv_igre = [
    'indeks_igre', 'prvi_igralec', 'prvi_id', 'drugi_igralec',
    'drugi_id', 'izid', 'stevilo_potez', 'leto', 'kraj',
    'odprtje_neka_stevilka', 'odprtje'
]

imena_polj_csv_igralci = [
    'id', 'ime', 'letnica_rojstva', 'drzava_rojstva',
    'stevilo_iger_v_bazi', 'zacetek', 'konec',
    'zmage', 'porazi', 'remiji',
    'delez_zmag', 'kvaliteta'
]

orodja.zapisi_csv(igre, imena_polj_csv_igre, 'izluscene_igre.csv')
orodja.zapisi_csv(igralci, imena_polj_csv_igralci, 'izlusceni_igralci.csv')
orodja.zapisi_json(igre, 'izluscene_igre.json')
orodja.zapisi_json(igralci, 'izlusceni_igralci.json')