# Kratke igre šaha

Podatke sem zajel s strani [chessgames.com](https://www.chessgames.com/).

## Zajeti podatki:

Zajel sem 5000 iger, ki ustrezajo pogojem: odigrane so po letu 1980, ne končajo se z remijem in imajo največ 15 potez. Nato sem pobral še podatke igralcev, ki so sodelovali v vsaj eni od zajetih iger. Njih je 7567. Podatki o igrah so v datotekah `izluscene_igre.json` in `izluscene_igre.csv`, o igralcih pa v `izlusceni_igralci.json` in `izlusceni_igralci.csv`.

### O vsaki igri sem pobral:
- igralca, ki sta jo odigrala,
- izid,
- kraj, kjer je potekala,
- odprtje (z [ECO](https://en.wikipedia.org/wiki/Encyclopaedia_of_Chess_Openings) oznako), s katerim se je začela.

### O slehernem igralcu pa:
- ime,
- aktivna leta,
- število vseh iger v bazi,
- letnico in državo rojstva,
- skupno število zmag, porazov in remijev ter delež zmag,
- FIDE rating kot kvaliteto.

## Delovne hipoteze:
- Večkrat zmaga igralec z belimi figurami.
- Pri odprjih D ali E pogosteje zmaga črni igralec.
- Odprtje A je pogostejše pri boljših igralcih.
- Igralci, ki so začeli igrati pred 1980, imajo manjši delež remijev kot ostali.
