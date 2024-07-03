"""
Constante = 'Variáveis" que não vão mudar
Muitas condições no mesmo if (Ruim)
    <- Contagem de complexidade (Ruim)
"""
velocidade = 66 #Velocidade atual do carro
local_carro = 100 #Local em que o carro está na estrada

RADAR_1 = 60 #velocidade maxima do radar 1
LOCAL_1 = 100 #Local onde o radar 1 está
RADAR_RANGE = 1 #A distancia onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro<= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar1 = vel_carro_pass_radar_1 and carro_passou_radar1



if vel_carro_pass_radar_1:
    print('Velocidade do carro passou do radar 1')

if carro_passou_radar1:
    print('Carro passou no radar 1')

if carro_multado_radar1:
    print(' A velocidade do carro foi maior que a permitida')