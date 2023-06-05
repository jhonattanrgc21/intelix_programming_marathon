import java.util.Scanner;

public class G{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String expresion = sc.nextLine();
        String resultado = "";
        String letraStr;
        for (char letra : expresion.toCharArray()) {
            letraStr = String.valueOf(letra);
            if(!resultado.contains(letraStr)){
                resultado = resultado.concat(letraStr);
            }
        }

        System.out.println(resultado);
        sc.close();
    }
}