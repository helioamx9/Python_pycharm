
import math
segundos = int(input('Por favor, entre com o número de segundos que deseja converter:'))

minutos = segundos/60
horas = minutos/60
dias = horas/24
restSeg=segundos%60
restMin = math.floor(minutos%60)
restHoras = math.floor(horas%24)

print(f'{dias:.0f} dias, {restHoras %60:.0f} horas, {restMin:.0f} minutos e {restSeg} segundos.')
