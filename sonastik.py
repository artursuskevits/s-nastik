
from mymodul import*
laused=[]
russian=[]
english=[]
russian=loe_faelist("russian.txt")
print(russian)
english=loe_faelist("english.txt")
print(english)
while True:
    v=int(input("1-add all changes in txt file\n2 - tarnslite sona\n3-lisa sona \n4-muuda sona \n5-test \n6 kuula sona"))
    if v==1:
        for jj in range (len(russian)):
            line=russian[jj]
            laused.append(line)
        Kirjuta_failise("russian.txt",laused)
        laused=[]
        for j in range (len(english)):
            line=english[j]
            laused.append(line)
        Kirjuta_failise("english.txt",laused)
    elif v==2:
        russian, english=translate(russian, english)
    elif v==3:
        russian, english=addsona(russian, english)
    elif v==4:
        russian, english=mudasona(russian, english)
    elif v==5:
        russian, english=test(russian, english)
        for jj in range (len(russian)):
            line=russian[jj]
            laused.append(line)
        Kirjuta_failise("laused.txt",laused)
    elif v==6:
        laused=[]
        sona = choose_sona(russian, english)
        for jj in range (len(russian)):
            if sona == english[jj]:
                text = sona
                laused.append(text)
                #text : kõik elemendis järjendis
                Heli(laused[0],"en")
        text = sona
        laused.append(text)
        #text : kõik elemendis järjendis
        Heli(laused[0],"ru")

        