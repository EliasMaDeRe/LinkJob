'''
Author: "Space Team"
Date: 12/02/2022
Description: Printing the upper diagonal of a matrix traversed by rows
'''

#Input
range = [0,1,2,3,4]
Dimension = 5
filas = 0
columnas = 0

#Algorithm
for columnas in range:
    Dimension = Dimension-1  
    for filas in range:
        if filas < Dimension:
            print(f"      ", end= "")       

    for filas in range:
        if filas >= Dimension:
            print(f"({filas},{columnas}) ", end= "") 
       
    print(" ")   

#Output       