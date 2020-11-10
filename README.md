# Kratke igre šaha

Podatke sem zajel s strani [chessgames.com](https://www.chessgames.com/).

## Zajeti podatki:

Zajel sem 5000 iger, ki ustrezajo pogojem: odigrane so po letu 1980, končajo se z remijem in imajo največ 15 potez. Nato sem pobral še podatke igralcev, ki so sodelovali v vsaj eni od zajetih iger. Njih je 7567. Podatki o igrah so v datotekah `izluscene_igre.json` in `izluscene_igre.csv`, o igralcih pa v `izlusceni_igralci.json` in `izlusceni_igralci.csv`.

### O vsaki igri sem pobral:
- igralca, ki sta jo odigrala,
- izid,
- kraj, kjer je potekala, in
- odprtje, s katerim se je začela.

### O slehernem igralcu pa:
- ime,
- aktivna leta,
- število vseh iger v bazi,
- letnico in državo rojstva,
- skupno število zmag, porazov in remijev ter delež zmag in
- FIDE rating kot kvaliteto.

## Delovne hipoteze:
- Igralci nekaterih narodnosti imajo pogosteje kratke igre.
- Igre, ki se začnejo z določenimi otvoritvami, se končajo hitreje.
- Večkrat zmaga igralec z belimi figurami.