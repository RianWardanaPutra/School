import java.util.*;
import java.io.*;
import java.security.*;

public class RandomNumGenerator {
    public static void main(String[] args)
            throws FileNotFoundException, NoSuchAlgorithmException, NoSuchProviderException, IOException {
        String fileName;
        Scanner inputNum = new Scanner(System.in);
        System.out.println("Input file name: ");
        fileName = inputNum.nextLine();
        File randomNum = new File(fileName + ".txt");
        PrintWriter inRand = new PrintWriter(
                new BufferedWriter(new OutputStreamWriter(new FileOutputStream(randomNum), "UTF-8")), false);
        SecureRandom randomer = SecureRandom.getInstance("SHA1PRNG", "SUN");
        System.out.println("Enter the number: ");
        int request = inputNum.nextInt();
        for (int counter = 1; counter <= request; counter++) {
            inRand.println(randomer.nextInt());
        }
        inRand.close();
        inputNum.close();
    }
}
