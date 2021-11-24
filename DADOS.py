from random import randint
may=6
min=1
par=0
impar=0
for i in range (0,1):
    dado1=randint(1,6)
    dado2=randint(1,6)
    dado3=randint(1,6)
    dado4=randint(1,6)
    dado5=randint(1,6)
    if dado1>dado2:
        may=dado1
        min=dado2
        pos=i
    if dado2>dado3:
        may=dado2
        min=dado3
        pos=i
    if dado3>dado4:
        may=dado3
        min=dado4
        pos=i
    if dado4 > dado5:
        may=dado4
        min=dado5
        pos=i
    # DEMOSTRAR SI SON PAR O IMPAR
    if dado1 % 2 == 0:
        par = par+1
    else:
        impar =+ 1

    if dado2 % 2 == 0:
        par = par+1
    else:
        impar =+ 1

    if dado3 % 2 == 0:
        par = par+1
    else:
        impar =+ 1

    if dado4 % 2 == 0:
        par = par+1
    else:
        impar = impar + 1

    if dado5 % 2 == 0:
        par = par + 1
    else:
        impar =impar+ 1
    print("Los pares: ",par)
    print("Los impares: ",impar)

sumaTotal=dado1+dado2+dado3+dado4+dado5
print("Suma de todos los dados es: ",sumaTotal)
print("El mayor es: ",may)
print("El menor es: ",min)
