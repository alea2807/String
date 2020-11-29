str=(input("dati un sir de caractere:"))
#caractere
c=0
for i in str:
    if i.isalnum():
        continue
    if i.isspace():
        continue
    else:
        c+=1
print(c)