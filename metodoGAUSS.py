from fractions import Fraction

def transformarAfraccion(i,j):
    #transformar en una matriz de fraciones
    for i in range(m):
        for j in range(n):
            matriz[i][j]=Fraction(matriz[i][j],1)

def CoeficienteUnitario(celda, renglon):
    #convertir celdas diagonales en 1
    if celda !=0 :
        for j in range(n):
            if matriz[renglon][j] != 0:
                a=Fraction(1/celda)
                matriz[renglon][j]=a*matriz[renglon][j]

def sumarRenglones(renglonA,renglonB):
    #inverso aditivo
    inv=matriz[renglonB][renglonA]
    for j in range (n):
        matriz[renglonB][j]=matriz[renglonB][j] - matriz[renglonA][j]*inv

m=int(input(" digite numero de variables -> "))
n=m+1 #matriz aumentada

matriz = []
vectorSolucion = []
for i in range (m):
    renglon=[]
    print("\n ***ingrese coeficientes renglon [" , i +1 ,"] ***")
    for j in range(n):
        print(" celda[", i+1,j+1,"]  ")
        renglon.append(int(input(" -> ")))
    matriz.append(renglon)
    print(matriz)


transformarAfraccion(m,n)
print(matriz)

for i in range(m):
    CoeficienteUnitario(matriz[i][i],i)
    for j in range(m):
        if i!=j:
            sumarRenglones(i,j)

for i in range(m):
    if matriz[i][m].numerator % matriz[i][m].denominator==0:
        a=int(matriz[i][m])
        vectorSolucion.append(a)
    else:
        vectorSolucion.append(str(matriz[i][m]))


print(" solucion : ", vectorSolucion)











