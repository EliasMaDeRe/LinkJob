public class Columnas_DI_I{
    public static void main(String[] ars){

        int DIMENSION = 5;
        int Matriz[][] = new int[DIMENSION][DIMENSION];

        for(int Columnas = 0; Columnas < DIMENSION; ++Columnas){
            for(int Filas = 0; Filas <= Columnas; ++Filas){
                                
                System.out.print(Columnas+","+Filas+" ");

            }

            System.out.println();

        }

    }
}