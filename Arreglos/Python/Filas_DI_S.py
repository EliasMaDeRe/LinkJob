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
for filas in range:
    Dimension = Dimension-1    
    for columnas in range:
        if columnas <= Dimension:
            print(f"({filas},{columnas}) ", end= "")    
    print(" ")   

#Output        