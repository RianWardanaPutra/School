import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.util.Scanner;

class CreateSortedarray {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner sc = new Scanner(System.in);
        System.out.println("Masukkan nama file:");
        String fileName = sc.nextLine();
        File file = new File(fileName + ".txt");
        PrintWriter writer = new PrintWriter(new BufferedWriter(new OutputStreamWriter(new FileOutputStream(file))), false);
        System.out.println("Masukkan jumlah angka:");
        int size = sc.nextInt();
        int[] arr = new int[size];
        for(int i = arr.length - 1; i >= 0; i--) {
            writer.println(i);
        }
        sc.close();
        writer.close();
    }
}