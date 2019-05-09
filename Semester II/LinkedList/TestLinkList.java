import java.util.Scanner;

public class TestLinkList{
    public static void main(String[] args){
        LinkedListGW ll = new LinkedListGW();
        ll.insertFirst(10);
        ll.insertLast(5);
        ll.insertFirst(3);
        ll.insertLast(13);
        Scanner sc = new Scanner(System.in);
        int search = sc.nextInt();
        System.out.println(ll.contains(search));
        sc.close();
    }
}