def expande_caracter(texto):
    resultado = ''
    i = 0
    while i < len(texto):
        if texto[i] == '-':
            anterior = texto[i-1]
            proximo = texto[i+1]
            for codigo in range(ord(anterior) + 1, ord(proximo)):
                resultado += chr(codigo)
        else:
            resultado += texto[i]
        i += 1
    return resultado

print(expande_caracter("adfG-Klm"))