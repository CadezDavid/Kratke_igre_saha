import re
import orodja

def poisci_podatke_igralca(indeks):

	vsi_podatki = ['letnica_rojstva', 'drzava_rojstva', 'zmage', 'porazi', 'remiji', 'delez_zmag', 'stevilo_iger_v_bazi', 'aktivna_leta', 'kvaliteta']

	vzorec_1 = (
		r'<font size=-2>\(.*?(?P<letnica_rojstva>\d{4}).*?\)(?P<drzava_rojstva>.*)</font>'
		r'</font></td>\n'
		r'<td background="/chessimages/chessgamesbio\.gif" width=212 align=RIGHT>'
	)

	vzorec_2 = (
		r'Overall record: <B>\+(?P<zmage>\d+) -(?P<porazi>\d+) =(?P<remiji>\d+) \((?P<delez_zmag>\d{2}\.\d)<font size=-1>%</font>\)\*</B>'
	)

	vzorec_3 = (
		r'Number of games in database: <B>(?P<stevilo_iger_v_bazi>.*)</B><br>'
	)

	vzorec_4 = (
		r'Years covered: <B>(?P<aktivna_leta>.*)</B><br>'
	)
	
	vzorec_0 = (
		r'Last FIDE rating: <B>(?P<kvaliteta>\d*)</B>'
	)

	with open(f'datoteke_igralci/{indeks}.html') as f:
		vsebina = f.read()

	profil_igralca = dict()

	for vzorec in [vzorec_0, vzorec_1, vzorec_2, vzorec_3, vzorec_4]:
		for zadetek in re.finditer(vzorec, vsebina):
			profil_igralca.update(zadetek.groupdict())

	for podatek in vsi_podatki:
		if podatek not in profil_igralca:
			profil_igralca[podatek] = None

	profil_igralca['drzava_rojstva'] = orodja.odstrani_vsebino_v_oklepajih(profil_igralca['drzava_rojstva'])

	profil_igralca.update(orodja.aktivna_leta(profil_igralca['aktivna_leta']))
	profil_igralca.pop('aktivna_leta')

	return profil_igralca