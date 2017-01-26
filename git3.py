#24.01.2017
#Þórður Jónatansson
#Git/pycharm verkefni


#Dæmi 1
tala1=int(input("Sláðu inn tölu"))
tala2=int(input("Sláðu inn aðra tölu"))
print("tölurnar lagðar saman : ",tala1+tala2)
print("tölurnar margfaldaðar : ",tala1*tala2)


#Dæmi 2
fornafn=input("Sláðu inn fornafn : ")
eftirnafn=input("Sláðu inn eftirnafn : ")
print("Halló ",fornafn, eftirnafn)

#Dæmi 3
hastafir=0
lastafir=0
laghastaf=0

texti=input("Sláðu inn texta : ")
for i in range(len(texti)):
    if texti[i].isupper():
        hastafir=hastafir+1

    if texti[i].islower():
        lastafir=lastafir+1

print(texti)
print("það eru",hastafir,"Hástafir og",lastafir,"lástafir")
