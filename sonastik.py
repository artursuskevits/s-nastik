from fnmatch import translate
from mymodul import*
laused=["hi guys"]
russian=[]
english=[]
while True:
    v=int(input("1-loeme failis\n2 - tarnslite sona\n3-lisa sona \n4-muuda sona"))
    if v==1:
        russian=loe_faelist("russian.txt")
        for line in russian:
            print(line)
        print(russian)
        english=loe_faelist("english.txt")
        for line in english:
            print(line)
        print(english)
    elif v==2:
        russian, english=translate(russian, english)
    elif v==3:
        russian, english=addsona(russian, english)
    elif v==4:
        russian, english=mudasona(russian, english)

#    elif v==2:
#        line=input("Lisa lause: ")
#        laused.append(line)
#        Kirjuta_failise("laused.txt",laused)
#    elif v==3:
#        text=""
#        for line in laused:
#            text=text+" "+line
#        #text : kõik elemendis järjendis
#        ind=int(input("Number: "))
#        Heli(laused[ind],"et")

        