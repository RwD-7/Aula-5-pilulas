def simularCrecimento(pop,taxa,limite):
    anos = 0
    while pop <= limite:
        pop = pop * (1+taxa/100)
        anos += 1
        return anos
    
    
#main
p = float(input("populacao:"))
t = float(input("taxa%:"))    
l = float(input("limite:"))    

print(F"Anos={simularCrecimento(p,t,l)}")