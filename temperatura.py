temperatura = int(input('digite a temperatura da carne: '))

if temperatura < 48:
  print('Carne bem crua!')
elif temperatura in range(48, 54):
  print('Carne selada!')
elif temperatura in range(54, 59):
  print('Carne ao ponto para mal!')
elif temperatura in range(59, 64):
  print('Carne ao ponto!')
elif temperatura in range(64, 70):
  print('Carne ao ponto para bem!')
elif temperatura >= 71:
  print('Bem passada!')