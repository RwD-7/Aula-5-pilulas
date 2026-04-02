def calcularNotas():
    n1 = float(input("n1: "))
    n2 = float(input("n2: "))
    n3 = float(input("n3: "))
    
    media = (n1+n2+n3) /3
    if media <6:
        rec = float(input("nota da rec: "))
        media = (media + rec)/2
        return media

#main
m = calcularNotas()
if m >= 6:
    print("aprovado")
else:
    print("Reprovado")        