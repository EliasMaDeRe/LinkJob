package Java;
public class Columnas_D_S {
    
    public static void main (String[] args){
        int dimension = 5;
        int arreglo[][]= new int [dimension][dimension];
        int filas=0, columnas=0;
    
        for (columnas=0;columnas<dimension; columnas ++){
            for (filas=0; filas<dimension; filas++){
                if (filas<columnas){
                    System.out.print("      ");
                }else{
                    System.out.print("("+columnas+","+filas+") ");
                }
                
             }   
        System.out.println(" "); 
        }
    }
    
}
