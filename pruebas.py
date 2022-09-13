from time import sleep

HIGH = '11111111'
LOW  = '00000000'


def highOrLow(number, value):
  return HIGH if number & value else LOW

def marquesina(ledEncendido : int):
  print(12, highOrLow(ledEncendido, 0x00000001))
  print(16, highOrLow(ledEncendido, 0x00000002))
  print(18, highOrLow(ledEncendido, 0x00000004))
  print(22, highOrLow(ledEncendido, 0x00000008))
  print(24, highOrLow(ledEncendido, 0x00000010))
  print(26, highOrLow(ledEncendido, 0x00000020))
  print(32, highOrLow(ledEncendido, 0x00000040))

corrNumber = 1
goingLeft  = True

while True:
  sleep(1)
  marquesina(corrNumber)
  print('-'*7)
  if goingLeft:
    corrNumber <<= 1
  else:
    corrNumber >>= 1
  if corrNumber == 64 or corrNumber == 1:
    goingLeft = not goingLeft
  
    
  