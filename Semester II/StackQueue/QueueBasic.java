import java.util.InputMismatchException;
import java.util.Scanner;

public class QueueBasic{
    public static void main(String[] args) {
        long numTemp;
        int queueSize;
        int numChoice = 0;
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter queue size: ");
        queueSize = sc.nextInt();

        QueueInit queue = new QueueInit(queueSize);

        while (numChoice != 4) {
            try{
                System.out.println("\n1: Enqueue\n2: Dequeue\n3: Show queue list\n4: End\n");
                System.out.print("Enter command: ");
                numChoice = sc.nextInt();
                switch (numChoice){
                    case 1:
                        if(queue.isFull())
                            System.out.println("Queue is full");
                        else{
                            System.out.print("Enter number: ");
                            numTemp = sc.nextInt();
                            queue.insert((long)numTemp);
                        }
                        break;
                    case 2:
                        if (queue.isEmpty())
                            System.out.println("Queue is empty");
                        else {
                            numTemp = queue.remove();
                            System.out.println("Dequeued number: " + numTemp);
                        }
                        break;
                    case 3:
                        System.out.println("Content of queue list: {" + queue.showList() + "}");
                        break;
                    case 4:
                        System.out.println("Thank you.");
                        sc.close();
                        return;
                    default:
                        System.out.println("Wrong command!");
                }
            }catch (InputMismatchException e){
                System.out.println("Please input integers.");
                sc.next();
            }
            
        }
    }
}