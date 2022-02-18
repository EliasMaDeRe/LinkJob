/*
Author: Velentina Ortiz Porras
Date: 15/02/2022
Description: Leer un arreglo donde imprima los valores hacia abajo de la diagonal principal por columnas 
*/

#include <stdio.h>

int main(int argc, char const *argv[])
{
 int dimension = 5;
 int filas, columnas;

 for (filas = 0; filas < dimension; filas++){

     for (columnas = filas; columnas < dimension; columnas++){

            if(filas + columnas <= 8){
             printf("[%d,%d]", filas, columnas);
            }
             else {
          printf("     "); 
        }     
     }
     printf("\n");
 }
    return 0;
}
