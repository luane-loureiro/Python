#calculo da distancia entre 2 pontos
#distancia = raiz de (x2 - y1) **2 + (y2 -y1) **2

import math

x1 , x2 = map (float, input ("digite as cordenadas x1 e x2 ").split())
y1 , y2 = map (float, input ("digite as cordenadas y1 e y2 ").split())

distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print(f"A distancia é {distancia:.4f}")

input("Pressione Enter para sair...")

