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

from gtts import gTTS
import os
def Heli(text:str, keel:str):
    obj=gTTS(text=text, lang=keel,slow=False).save("heli.mp3")
    os.system("heli.mp3")
