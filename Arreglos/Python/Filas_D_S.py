'''
Author: "Space Team"
Date: 12/02/2022
Description: Printing the upper diagonal of a matrix traversed by rows
'''

#Input
range = [0,1,2,3,4]
filas = 0
columnas = 0

#Algorithm
for filas in range:
    for columnas in range:
        if columnas < filas:
            print("      ", end= "")
            
    for columnas in range:
        if columnas >= filas:
            print(f"({filas},{columnas}) ", end= "")
    print(" ")   

#Output        


