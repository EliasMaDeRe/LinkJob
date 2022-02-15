#define DIMENSION 5

#include <stdio.h>

int main() {
    int arreglo[DIMENSION][DIMENSION];
        int filas = 0, columnas = 0;

        for (filas = 0; filas < DIMENSION; filas++) {

            for (columnas = 0; columnas < DIMENSION; columnas++) {

                if (columnas + filas >= DIMENSION - 1) {
                    printf("(%d,%d) ", filas, columnas);
                }
                else{
                    printf("      ");
                }
            }

            printf("\n");
        }
    return 0;
}