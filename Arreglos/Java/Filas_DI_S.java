public class Filas_DI_S{
    public static void main(String[] ars){

        int DIMENSION = 5;
        int Matriz[][] = new int[DIMENSION][DIMENSION];

        for(int Filas = 0; Filas < DIMENSION; ++Filas){
            for(int Columnas = 0; Columnas < DIMENSION; ++Columnas){
                
                if(Columnas < Filas){
                    System.out.print("    ");
                }else{
                System.out.print(Filas+","+Columnas+" ");
                }
            }

            System.out.println();

        }

    }
}