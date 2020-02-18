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

    public boolean isFull() {
        return (currentSize == maxSize);
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

    public Node replaceTop(int key) {
        Node top = heapArray[0];
        Node newTop = new Node(key);
        heapArray[0] = newTop;
        trickleDown();
        return top;
    }

    public int peek() {
        return heapArray[0].getKey();
    }

    public int[] heapSort() {
        int[] result = new int[maxSize];
        int counter = currentSize - 1;
        while (currentSize > 0) {
            result[counter] = extract().getKey();
            for (int i = 0; i < currentSize; i++) {
                System.out.print("[" + i + "]: " + heapArray[i].getKey() + " ");
            }
            System.out.println();
            counter--;
        }
        return result;
    }
}

class Tester {
    public static void main(String[] args) {
        int jumlah = 0;
        System.out.println("MaxHeap first try");
        Scanner sc = new Scanner(System.in);
        System.out.print("\nBuilding array of random integers\nEnter the number of elements:");
        jumlah = sc.nextInt();
        int[] arrayAwal = new int[jumlah];
        MaxHeap h1 = new MaxHeap(jumlah);
        for (int i = 0; i < jumlah; i++) {
            arrayAwal[i] = ((int) (Math.random() * 100) + 1);
        }
        for (int i : arrayAwal) {
            h1.insert(i);
        }

        int menu = 0;
        while (menu != 7) {

            System.out.print("\nMenu:\n[1] Show generated array\n[2] Show Max Heap\n[3] Delete key from heap"
                    + "\n[4] Insert new key to heap\n[5] Replace root of heap\n[6] Heap sort\n[7] Exit\n\n");
            menu = sc.nextInt();
            switch (menu) {
            case 1:
                System.out.println("Generated array: ");
                for (int i = 0; i < arrayAwal.length; i++) {
                    System.out.print("[" + i + "]: " + arrayAwal[i] + " ");
                }
                System.out.println();
                break;
            case 2:
                System.out.println("Generated heap: ");

                for (int i = 0; i < h1.getSize(); i++) {
                    System.out.print("[" + i + "]: " + h1.getArray()[i].getKey() + " ");
                }
                System.out.println();
                break;
            case 3:
                if (h1.isEmpty()) {
                    System.out.println("Heap is empty, cannot delete key if there is no key!");
                } else {
                    System.out.println("Delete key");
                    System.out.println(
                            "\nThis will delete top-most heap member, which is the biggest value in max heap.");
                    System.out.println("Deleted: " + (h1.extract().getKey()));
                }
                System.out.println();
                break;
            case 4:
                System.out.print("\nInsert new key to heap.\nInsert new key: ");
                int newKey = sc.nextInt();
                h1.insert(newKey);
                System.out.println(newKey + " inserted!");
                System.out.println();
                break;
            case 5:
                System.out.print("Replace root of heap, thus more efficient than deleting and then inserting new key."
                        + "\nInsert new key: ");
                int newRoot = sc.nextInt();
                h1.replaceTop(newRoot);
                System.out.println(newRoot + " replaced the previous root!");
                System.out.println();
                break;
            case 6:
                int[] sorted = h1.heapSort();
                System.out.print("\nHeap sort. Please note that this will remove all of heap's elements!\nSorted array:\n");
                for (int i = 0; i < sorted.length; i++) {
                    if (sorted[i] == 0) {
                        break;
                    }
                    System.out.print("[" + i + "]: " + sorted[i] + " ");
                }
                System.out.println();
                break;
            default:
                break;
            }
        }
        System.out.println("Thank you!");
        sc.close();
    }
}