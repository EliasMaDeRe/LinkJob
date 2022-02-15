public class Filas_DI_I{
    public static void main(String[] ars){

        int DIMENSION = 5;
        int Matriz[][] = new int[DIMENSION][DIMENSION];

        for(int Filas = 0; Filas < DIMENSION; ++Filas){
            for(int Columnas = 0; Columnas <= Filas; ++Columnas){
                                
                System.out.print(Filas+","+Columnas+" ");

            }

            System.out.println();

        }

    }
}