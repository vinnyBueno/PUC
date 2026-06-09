def eliminar_espacoBraco (texto):
    resultado = ''
    i = 0
    while i < len(texto):
        if texto[i] == ' ':

            if resultado == '':
                i += 1
            elif resultado[-1] == ' ':
                i += 1
            else:
                resultado += texto[i]
                i += 1
        else:
            resultado += texto[i]
            i += 1

    return resultado

print(eliminar_espacoBraco("python"))