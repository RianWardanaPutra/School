import java.util.ArrayList;
import java.util.Collections;

class NumberGen {
    static int max = 50000000;
    static int count = 40000001;
    public static void main(String[] args) {
        ArrayList<Integer> number = new ArrayList<>();
        while (count <= max) {
            number.add(count);
            count++;
        }
        Collections.shuffle(number);
        for (long e : number) {
            System.out.println(e);
        }
    }
}