import java.util.*;
import java.io.*;
import java.security.*;

public class RandomNumGenerator{
    public static void main(String[] args) throws FileNotFoundException,NoSuchAlgorithmException,NoSuchProviderException,IOException{
        File randomNum= new File("randomNumber500m.txt");
        PrintWriter inRand= new PrintWriter(new BufferedWriter(new OutputStreamWriter(new FileOutputStream(randomNum),"UTF-8")),false);
        SecureRandom randomer= SecureRandom.getInstance("SHA1PRNG","SUN");
        Scanner inputNum=new Scanner(System.in);
        int request=inputNum.nextInt();
        for(int counter=1;counter<=request;counter++){
            inRand.println(randomer.nextInt());
        }
        inRand.close();
        inputNum.close();
    }
}