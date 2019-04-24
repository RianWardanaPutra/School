import java.util.Scanner;

class Node {
    private int data;

    public Node(int key) {
        this.data = key;
    }

    public int getKey() {
        return this.data;
    }

    public void setKey(int key) {
        this.data = key;
    }
}

class MaxHeap {
    private Node[] heapArray;
    private int maxSize;
    private int currentSize;

    public Node[] getArray() {
        return heapArray;
    }

    public MaxHeap(int max) {
        this.maxSize = max;
        this.currentSize = 0;
        heapArray = new Node[maxSize];
    }

    public boolean isEmpty() {
        return (currentSize == 0);
    }

    public int getSize() {
        return this.currentSize;
    }

    public boolean insert(int key) {
        if (currentSize == maxSize)
            return false;
        Node newNode = new Node(key);
        heapArray[currentSize] = newNode;
        trickleUp(currentSize++);
        return true;
    }

    public Node extract() {
        if (isEmpty()) {
            return null;
        } else {
            Node temp = this.heapArray[0];
            this.heapArray[0] = this.heapArray[--currentSize];
            trickleDown();
            return temp;
        }
    }

    public void trickleDown() {
        int parent = 0;
        int leftChild = (parent * 2) + 1;
        int rightChild = leftChild + 1;
        Node temp = heapArray[parent];
        int maxChild = (heapArray[leftChild].getKey() >= heapArray[rightChild].getKey()) ? leftChild : rightChild;
        while (maxChild < currentSize - 1 && temp.getKey() < heapArray[maxChild].getKey()) {
            heapArray[parent] = heapArray[maxChild];
            parent = maxChild;
            leftChild = (parent * 2) + 1;
            rightChild = leftChild + 1;
            if (leftChild < maxSize && rightChild < maxSize) {
                maxChild = (heapArray[leftChild].getKey() >= heapArray[rightChild].getKey()) ? leftChild : rightChild;
            } else if (rightChild >= maxSize && leftChild < maxSize) {
                maxChild = leftChild;
            } else {
                maxChild = rightChild;
            }
        }
        heapArray[parent] = temp;
    }

    public void trickleUp(int index) {
        int parent = (index - 1) / 2;
        Node bottom = heapArray[index];
        while (index > 0 && bottom.getKey() > heapArray[parent].getKey()) {
            heapArray[index] = heapArray[parent];
            index = parent;
            parent = (parent - 1) / 2;
        }
        heapArray[index] = bottom;
    }

    public Node replaceTop (int key) {
        Node top = heapArray[0];
        Node newTop = new Node(key);
        heapArray[0] = newTop;
        trickleDown();
        return top;
    }

    public int peek () {
        return heapArray[0].getKey();
    }

    public int[] heapSort() {
        int[] result = new int[maxSize];
        int counter = 0;
        while (currentSize > 0) {
            result[counter] = extract().getKey();
            counter++;
        }
        return result;
    }
}

class Tester {
    public static void main(String[] args) {
        System.out.println("MaxHeap first try");
        Scanner sc = new Scanner(System.in);
        System.out.print("\nMenu:\n1. Build random array of ints\n2. Build Max Heap\n3. Delete key from heap"
                            + "\n4. Insert new key to heap\n5. Replace root of heap\n6. View array\n7. Heap Sort");
        int menu = sc.nextInt();
        switch (menu) {
            case 1:
                System.out.println("Building array of random integers\nEnter the number of elements:");
                int jumlah = sc.nextInt();
                MaxHeap h1 = new MaxHeap(jumlah);
                int[] arrayAwal = new int[jumlah];
                for (int i = 0; i < menu; i++) {
                    arrayAwal[i] = ((int) (Math.random() * 100) + 1);
                }
                break;
        
            default:
                break;
        }
        System.out.print("Array awal: ");
        for (int i : arrayAwal) {
            System.out.print(i + " ");

            h1.insert(i);
        }

        System.out.println();

        for (int i = 0; i < h1.getSize(); i++) {
            System.out.print("[" + i + "]: " + h1.getArray()[i].getKey() + ",  ");
        }
        System.out.println("\nDelete key");
        System.out.println("Deleted: " + (h1.extract().getKey()));
        System.out.println("Array: ");
        for (int i = 0; i < h1.getSize(); i++) {
            System.out.print("[" + i + "]: " + h1.getArray()[i].getKey() + ",  ");
        }
        System.out.println("\nDeleted: " + (h1.extract().getKey()));
        System.out.println("Array: ");
        for (int i = 0; i < h1.getSize(); i++) {
            System.out.print("[" + i + "]: " + h1.getArray()[i].getKey() + ",  ");
        }
        System.out.println("\nDeleted: " + (h1.extract().getKey()));
        System.out.println("Array: ");
        for (int i = 0; i < h1.getSize(); i++) {
            System.out.print("[" + i + "]: " + h1.getArray()[i].getKey() + ",  ");
        }
        System.out.print("\nReplace root with: ");
        int newKey = (int) Math.random() * 100;
        System.out.println(newKey);
        h1.replaceTop(newKey);
        System.out.println("Array: ");
        for (int i = 0; i < h1.getSize(); i++) {
            System.out.print("[" + i + "]: " + h1.getArray()[i].getKey() + ",  ");
        }
        System.out.print("\nReplace root with: ");
        newKey = ((int) (Math.random() * 100) + 1);
        System.out.println(newKey);
        h1.replaceTop(newKey);
        System.out.println("Array: ");
        for (int i = 0; i < h1.getSize(); i++) {
            System.out.print("[" + i + "]: " + h1.getArray()[i].getKey() + ",  ");
        }
        sc.close();
    }
}