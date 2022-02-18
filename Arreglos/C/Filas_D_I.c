/*
Author: Velentina Ortiz Porras
Date: 15/02/2022
Description: Leer un arreglo donde imprima los valores hacia abajo de la diagonal principal por filas 
*/

#include <stdio.h>

int main(int argc, char const *argv[])
{
 int dimension = 5;
 int filas, columnas;

 for (columnas = 0; columnas < dimension; columnas++){

     for (filas = 0; filas <= columnas; filas++){

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
