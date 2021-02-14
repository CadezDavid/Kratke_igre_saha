# Celotno datoteko sem vzel iz gradiv s predavanj
import csv
import json
import os
import requests
import sys
import re


def pripravi_imenik(ime_datoteke):
    '''Če še ne obstaja, pripravi prazen imenik za dano datoteko.'''
    imenik = os.path.dirname(ime_datoteke)
    if imenik:
        os.makedirs(imenik, exist_ok=True)


def shrani_spletno_stran(url, ime_datoteke, vsili_prenos=False):
    '''Vsebino strani na danem naslovu shrani v datoteko z danim imenom.'''
    try:
        print(f'Shranjujem {url} ...', end='')
        sys.stdout.flush()
        if os.path.isfile(ime_datoteke) and not vsili_prenos:
            print('shranjeno že od prej!')
            return
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        print('stran ne obstaja!')
    else:
        pripravi_imenik(ime_datoteke)
        with open(ime_datoteke, 'w', encoding='utf-8') as datoteka:
            datoteka.write(r.text)
            print('shranjeno!')


def vsebina_datoteke(ime_datoteke):
    '''Vrne niz z vsebino datoteke z danim imenom.'''
    with open(ime_datoteke, encoding='utf-8') as datoteka:
        return datoteka.read()


def zapisi_csv(slovarji, imena_polj, ime_datoteke):
    '''Iz seznama slovarjev ustvari CSV datoteko z glavo.'''
    pripravi_imenik(ime_datoteke)
    with open(ime_datoteke, 'w', encoding='utf-8') as csv_datoteka:
        writer = csv.DictWriter(csv_datoteka, fieldnames=imena_polj)
        writer.writeheader()
        for slovar in slovarji:
            writer.writerow(slovar)


def zapisi_json(objekt, ime_datoteke):
    '''Iz danega objekta ustvari JSON datoteko.'''
    pripravi_imenik(ime_datoteke)
    with open(ime_datoteke, 'w', encoding='utf-8') as json_datoteka:
        json.dump(objekt, json_datoteka, indent=4, ensure_ascii=False)

def nalozi_stran(url):
    odziv = requests.get(url)
    return odziv.text

def presledke_zamenjaj_z_under(niz):
    nov_niz = ''
    for znak in niz:
        if znak == ' ':
            nov_niz += '_'
        else:
            nov_niz += znak
    return nov_niz

def odstrani_vsebino_v_oklepajih(niz):
    if niz == None:
        return None
    else:
        nov_niz = ''
        stevec = 0
        for znak in niz:
            if znak == '(':
                    stevec += 1
            if stevec > 0:
                if znak == ')':
                    stevec -= 1
            elif stevec == 0:
                    nov_niz += znak
        return nov_niz

def strip_vse(slovar):
    for element in slovar:
        if slovar[element] != None:
            slovar[element] = slovar[element].strip()
    return slovar

def aktivna_leta(niz):
    if len(niz) == 4:
        return {'zacetek': niz, 'konec': niz}
    else:
        vzorec = r'(?P<zacetek>\d{4})\D*(?P<konec>\d{4})'
        for zadetek in re.finditer(vzorec, niz):
            return zadetek.groupdict()
