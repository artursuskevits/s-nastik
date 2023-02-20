from mymodul import*
laused=["hi guys"]
russian=[]
english=[]
while True:
    v=int(input("1-loeme failis\n2 - salvetama failise\n3-Tekst Helis"))
    if v==1:
        russian=loe_faelist("russian.txt")
        for line in russian:
            print(line)
            print(russian)
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

        