def verificarValores():
    anterior = float(input("leitura1:"))
    cresente = True 
    
    for i in range(4):
        atual = float(input(F"leitura{i+2}:"))
        if atual <= anterior:
            return False
        anterior = atual
    return True

#main
if verificarValores():
    print("crescente")
else:
    print("instavel")        