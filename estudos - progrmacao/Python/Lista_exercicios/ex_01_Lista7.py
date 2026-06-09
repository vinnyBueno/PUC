def acha_carchter_invisivel(texto):
    resultado = ""
    i = 0
    while i < len(texto):
        if texto[i] == '\\':
            if texto[i+1] == 'n':
                resultado += '\n'
                i += 2
            elif texto[i+1] == 't':
                resultado += '\t'
                i += 2
        elif texto[i] != '\\':
            resultado += texto[i]
            i += 1
    return resultado
print(acha_carchter_invisivel("Oi\\nMundo"))