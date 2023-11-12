altura = float(input('Qual sua altura em cm? '))
peso = float(input('Qual seu peso em KG: '))

imc = peso / (altura/100)**2
#numero**2 = elevado ao quadrado

print(imc)

if imc < 18.5:
  print(f'Magreza seu imc:{float(imc)}')
elif imc >= 18.5 and imc < 24.9:
  print(f'Normal seu imc: {float(imc)}')
elif imc >= 25 and imc < 29.9:
  print(f'Sobrepeso seu imc: {float(imc)}')
elif imc >= 30 and imc < 39.9:
  print(f'Obesidade seu imc: {float(imc)}')
else:
  print(f'Obesidade Grave! seu imc: {float(imc)}')