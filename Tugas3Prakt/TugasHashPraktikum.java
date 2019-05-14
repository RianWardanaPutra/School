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

    public int clusterCount() {
        boolean still = false;
        int cluster = 0;
        for(int counter = 0; counter < arraySize; counter++) {
            if(arrayData[counter] != -1 && !still) {
                counter++;
                still = true;
            } else if (arrayData[counter] == -1) {
                still = false;
            }
        }
        return cluster;
    }
}

class Tester {
    public static void main(String[] args) {
        Hashing obj1 = new Hashing(100);
        Scanner sc = new Scanner(System.in);
        System.out.println("Input number");
        int menu = sc.nextInt();
        switch(menu) {
            case 1:
                System.out.println("Load factor 0.3:");
                
                for(int i = 0; i < 30; i++) {
                    obj1.insertQuadratic((int)(Math.random() * 1000) + 1);
                }
        }
        sc.close();
    }
}