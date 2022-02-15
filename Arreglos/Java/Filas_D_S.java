package Java;
public class Filas_D_S {

    public static void main (String[] args){
        int dimension = 5;
        int arreglo[][]= new int [dimension][dimension];
        int filas=0, columnas=0;
    
        for (filas=0; filas<dimension; filas++){
            for (columnas=0;columnas<dimension; columnas ++){
                if (columnas<filas){
                    System.out.print("      ");
                }else{
                    System.out.print("("+filas+","+columnas+") ");
                }
                
             }   
        System.out.println(" "); 
        }
    }
    
}
