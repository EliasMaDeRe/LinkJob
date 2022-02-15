public class Columnas_DI_S{
    public static void main(String[] ars){

        int DIMENSION = 5;
        int Matriz[][] = new int[DIMENSION][DIMENSION];

        for(int Columnas = 0; Columnas < DIMENSION; ++Columnas){
            for(int Filas = 0; Filas < DIMENSION; ++Filas){
                
                if(Filas < Columnas){
                    System.out.print("    ");
                }else{              
                System.out.print(Columnas+","+Filas+" ");
                }
            }

            System.out.println();

        }

    }
}