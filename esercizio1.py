from random import randint
print("le percentuali dei voti dei due candidati  x e y sono:")
x = randint(1, 100)
y = (100-x)
print(x, y)

print(" lista dei candidati in ordine alfabetico: x, y")
if x > y :
    print(" lista dei candidati in ordine decrescente: x, y")
else:
    print(" lista dei candidati in ordine decrescente: y, x")