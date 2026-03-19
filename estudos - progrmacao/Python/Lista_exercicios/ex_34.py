"""Faça um programa em pyrhon que solicite a digitação de três valores representado,
respectivamente, as horas, os minutos e os segundos de um horário, verificando, a seguir se
os mesmos representam ou não um horárioa válido"""

print("Programa para valider se horas são válidas")

try:
    horas = int(input("\nDigite as horas: "))
    minutos = int(input("\nDigite os minutos: "))
    segundos = int(input("\nDigite os segundos: "))
except ValueError:
    print("\nSomente numeros sem vírgula devem ser digitados!")
else:
    if 0 <= horas <= 23 and 0 <= minutos <= 59 and 0 <= segundos <= 59:
        print("\nHorario valido!")
        print(f"\nSão {horas} horas, {minutos} minutos e {segundos} segundos!")
    else:
        print("\nHorario inválido!!")
