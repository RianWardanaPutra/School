public class QueueInit{
    private int maxSize;
    private long[] queArray;
    private int front;
    private int rear;
    private int nItems;

    QueueInit (int s) {
        maxSize = s;
        queArray = new long[maxSize];
        front = 0;
        rear = -1;
        nItems = 0;
    }

    void insert(long j){
        if (rear == maxSize - 1) {
            rear = -1;
        }
        queArray[++rear] = j;
        nItems++;
    }

    long remove(){
        long temp = queArray[front++];
        if (front == maxSize) {
            front = 0;
        }
        nItems--;
        return temp;
    }

    boolean isEmpty(){
        return (nItems == 0);
    }

    boolean isFull(){
        return (nItems == maxSize);
    }

    int size(){
        return nItems;
    }

    long peekFront(){
        return queArray[front];
    }

    String showList(){
        String temp = "";
        for (long i : queArray)
            temp += ("'" + i + "', ");
        return temp;
    }
}