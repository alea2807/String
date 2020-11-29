str=(input("dati un sir de caractere:"))
n=0
#c-cifre
for c in str:
    n+=c.isdecimal()
print(n)