def ValidarSenha(senha):
    if len(senha) < 8:
        return "senha invalida, muito curta."
    
    temnumero = False
    temMaiuscla = False 
    
    for c in senha:
        if c == " ":
            return 'senha invalida, nao pode ter espaços'
        if c >= '0' and c <= "9":
            temnumero = True 
        if c >= "A" and c <= "Z":
            temMaiuscla = True
    if not temnumero:
        return "a senha nao tem numeros"
    if not temMaiuscla:
        return "a senha nao tem letras maisuculas"
    
    return "senha valida"
               
#main
senha = input("digite a senha:")
r = ValidarSenha(senha)
print(r)