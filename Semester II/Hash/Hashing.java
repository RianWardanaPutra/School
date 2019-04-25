import java.util.Scanner;

class Hashing {
    int arraySize;
    int currentSize;
    int[] arrayData;

    public Hashing(int size) {
        currentSize = 0;
        this.arraySize = size;
        arrayData = new int[size];
        for (int i = 0; i < arraySize; i++) {
            arrayData[i] = -1;
        }
    }

    public boolean isTableFull() {
        return (currentSize == arraySize);
    }

    public int modMethod(int key, int mod) {
        return (key % mod);
    }

    public void insertQuadratic(int key) {
        int index = modMethod(key, arraySize);
        int i = 1;
        if (isTableFull()) {
            System.out.println("Array is full!");
            return;
        } else {
            while (arrayData[index] != -1) {
                index += i * i;
                if (index >= arraySize) {
                    index = index % arraySize;
                }
                i++;
            }
            arrayData[index] = key;
            currentSize++;
        }
    }

    public void printArray() {
        for (int i : this.arrayData) {
            System.out.print(i + " =>  ");
        }
    }
}

class Driver {
    public static boolean isPrime(int key) {
        if (key % 2 == 0 || key % 3 == 0)
            return false;
        for (int i = 5; i <= Math.sqrt(key); i += 6) {
            if (key % i == 0 || key % (i + 2) == 0)
                return false;
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("\nFirst time hashing\nEnter the number of array (the number should be prime): ");
        int size = sc.nextInt();
        while (!isPrime(size)) {
            System.out.println("Insert prime number!");
            size = sc.nextInt();
        }

        int menu = 0;
        Hashing hash1 = new Hashing(size);
        do {
            System.out.println("\nMenu:\n[1] Insert key\n[2] Show array\n[3] Insert random numbers\n[4] Exit");
            menu = sc.nextInt();
            switch (menu) {
            case 1:
                System.out.print("\nInsert key: ");
                int key = sc.nextInt();
                hash1.insertQuadratic(key);
                break;
            case 2:
                System.out.println("Created hash:");
                hash1.printArray();
                break;
            case 3:
                System.out.println("Input number of random keys: ");
                int number = sc.nextInt();
                for (int i = 0; i < number; i++) {
                    hash1.insertQuadratic((int) (Math.random() * 100) + 1);
                }
            default:
                break;
            }
        } while (menu != 4);
        System.out.println("Thank you!");

        sc.close();
    }

}