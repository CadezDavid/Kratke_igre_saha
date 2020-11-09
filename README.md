# Kratke igre šaha

Podatke bom zajel s strani [chessgames.com](https://www.chessgames.com/).

Zajeti podatki:
- Vse igre imajo zmagovalca
- Vse igre imajo največ 15 potez
- Zmage posameznik igralcev
- Število potez na igralca
- Narodnost igralcev
- Otvoritve

Delovne hipoteze:
- Igralci nekaterih narodnosti imajo pogosteje kratke igre
- Igre, ki se začnejo z določenimi otvoritvami, se končajo hitreje
- Večkrat zmaga igralec z belimi figurami

## Vsebina

V csv in json so isti podatki, v izlusceni_igralci.* so zbrani igralci, njihovo leto rojstva in nacionalnost, v izluscene_igre.* pa so zbrane igre, ki vsebujejo indeks_igre, prvi_igralec, drugi_igralec, izid, stevilo_potez, leto, kraj, odprtje_neka_stevilka, odprtje, letnica_prvega, letnica_drugega, drzava_prvega, drzava_drugega.