n = int(input('Número: '))
inv = 0
while n > 0:
  inv = inv * 10
  inv = inv + n % 10
  n = n // 10
print(inv)
