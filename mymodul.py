from random import*
def loe_faelist(fail:str)->list:
    """
    """
    f=open(fail,"r",encoding="utf-8-sig")
    järjend=[]
    for rida in f:
        järjend.append(rida.strip())
    f.close()
    return järjend 

def Kirjuta_failise(fail:str,jarjend:list):
    f=open(fail,"w",encoding="utf-8-sig")
    for line in jarjend:
        f.write(line+"\n")
    f.close()

from distutils.command.sdist import sdist
from gtts import gTTS
import os
def Heli(text:str, keel:str):
    obj=gTTS(text=text, lang=keel,slow=False).save("heli.mp3")
    os.system("heli.mp3")

def translate(r:list,e:list):
    rr=len(e)
    language = int(input("kui soovite tõlkida inglise keelest vene keelde, vajutage 1 \n kui soovite tõlkida vene keelest inglise keelde vajutage 2"))
    if language == 1:
        print(e)
        engsona = input("Kirjutage sõna, mida soovite vene keelde tõlkida.")
        for jj in range (rr):
            if engsona == e[jj]:
                print(r[jj])
                print(f"{engsona} on russian {r[jj]}")
    if language == 2:
        print(r)
        russona = input("Kirjutage sõna, mida soovite vene keelde tõlkida.")
        for jj in range (rr):
            if russona == r[jj]:
                print(e[jj])
                print(f"{russona} on english {e[jj]}")
    return r,e

def addsona (r:list,e:list):
    engsona = input("kirjutage inglise keeles sõna, mida soovite lisada")
    russona = input("kirjuta nüüd selle tõlge vene keelde")
    e.append(engsona)
    r.append(russona)
    print (r, e)
    return r, e

def mudasona (r:list,e:list):
    keel= int(input("kui soovid muuta ingliskeelset sõna kirjuta 1 \n kui soovid muuta venekeelset sõna kirjuta 2"))
    if keel ==1:
        rr=len(e)
        print(e)
        sona=input("kirjutage sõna, mida soovite muuta")
        for jj in range (rr):
             if sona == e[jj]:
                sonachange=input("kirjutage muudetud sõna")
                e.pop(jj)
                e.insert(jj, sonachange)
                break
    elif keel ==2:
        rr=len(e)
        print(r)
        sona=input("kirjutage sõna, mida soovite muuta")
        for jj in range (rr):
             if sona == r[jj]:
                sonachange=input("kirjutage muudetud sõna")
                r.pop(jj)
                r.insert(jj, sonachange)
                break
    return r, e

def test (r:list,e:list):
    oige = 0
    koik = 0
    rr=len(e)
    kuipalju=int(input("kui plaju sonad te tahate testiga,max7))))"))
    if kuipalju <=7:
        for j in range (kuipalju):
            random_word=choice(e)
            for jj in range (rr):
                if random_word == e[jj]:
                    answer=input(f"tõlgi {random_word} vene keelde")
                    if answer == r[jj]:
                        koik +=1
                        oige +=1
                    else:
                        koik +=1
    result = oige/koik * 100
    print(f"see reult on {result}%")
    return r, e


