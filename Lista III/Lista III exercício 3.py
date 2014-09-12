
a = 80000
b = 200000
anos = 0
while a <= b:
  a = a + a * 0.03  #Acumulador
  b = b + b * 0.015 #Acumulador
  anos = anos + 1   #Contador
print (anos)
