import java.util.Scanner;

class Hashing {
    private int arraySize;
    int currentSize;
    private int[] arrayData;

    public static int PRIME = 97;

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

    public void insertLinear(int key) {
        if (isTableFull()) {
            System.out.println("Array is full!");
            return;
        }
        int index = modMethod(key, arraySize);
        while (arrayData[index] != -1) {
            index++;
            if (index >= arraySize) {
                index %= arraySize;
            }
        }
        arrayData[index] = key;
        currentSize++;
    }

    public void insertQuadratic(int key) {
        if (isTableFull()) {
            System.out.println("Array is full!");
            return;
        }
        int index = modMethod(key, arraySize);
        int i = 1;    
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

    public int modMethod(int key, int mod) {
        return (key % mod);
    }

    public int modMethod2(int key, int mod) {
        return ((key % mod) + 1);
    }

    public void insertDoubleHashing(int key) {
        if (isTableFull()) {
            System.out.println("Array is full!");
            return;
        }
        int index = modMethod(key, arraySize);
        int i = 1;
        while (arrayData[index] != -1) {
            index = (modMethod(key, arraySize) + i * modMethod2(key, PRIME)) % arraySize;
            if (index == arraySize)
                index = 0;
            else if (index > arraySize)
                index = index % arraySize;
            if (index < 0)
                index += arraySize;
            i+=2;
        }
        arrayData[index] = key;
        currentSize++;
    }

    public void clearData() {
        for (int i = 0; i < arraySize; i++) {
            arrayData[i] = -1;
        }
        currentSize = 0;
    }

    public void printArray() {
        for (int i : this.arrayData) {
            System.out.print(i + " =>  ");
        }
    }

    public int clusterCount() {
        boolean still = false;
        int cluster = 0;
        for (int counter = 0; counter < arraySize; counter++) {
            if (arrayData[counter] != -1 && !still) {
                cluster++;
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
        Hashing obj1 = new Hashing(101);
        //Hashing obj1 = new Hashing(100);
        Scanner sc = new Scanner(System.in);
        System.out.println("Menu:\n[1] 0.3 load factor\n[2] 0.5 load factor"
                + "\n[3] 0.7 load factor\n[4] 0.9 load factor\nInput number");
        int menu = sc.nextInt();
        int[] number;
        switch (menu) {
        case 1:
            System.out.println("Load factor 0.3:");
            number = new int[30];
            for (int i = 0; i < 30; i++) {
                number[i] = (int) (Math.random() * 1000) + 1;
            }
            System.out.println("Linear probing.");
            for (int i : number) {
                obj1.insertLinear(i);
            }
            System.out
                    .println("Done.\nCluster count = " + obj1.clusterCount() + " clusters when using linear probing.");
            obj1.clearData();
            System.out.println("Quadratic probing.");
            for (int i : number) {
                obj1.insertQuadratic(i);
            }
            System.out.println(
                    "Done.\nCluster count = " + obj1.clusterCount() + " clusters when using quadratic probing.");
            obj1.clearData();
            System.out.println("Double hashing.");
            for (int i : number) {
                obj1.insertDoubleHashing(i);
            }
            System.out.println(
                    "Done.\nCluster count = " + obj1.clusterCount() + " clusters when using double hasing probing.");
            obj1.clearData();
            break;
        case 2:
            System.out.println("Load factor 0.5:");
            number = new int[50];
            for (int i = 0; i < 50; i++) {
                number[i] = (int) (Math.random() * 1000) + 1;
            }
            System.out.println("Linear probing.");
            for (int i : number) {
                obj1.insertLinear(i);
            }
            System.out
                    .println("Done.\nCluster count = " + obj1.clusterCount() + " clusters when using linear probing.");
            obj1.clearData();
            System.out.println("Quadratic probing.");
            for (int i : number) {
                obj1.insertQuadratic(i);
            }
            System.out.println(
                    "Done.\nCluster count = " + obj1.clusterCount() + " clusters when using quadratic probing.");
            obj1.clearData();
            System.out.println("Double hashing.");
            for (int i : number) {
                obj1.insertDoubleHashing(i);
            }
            System.out.println(
                    "Done.\nCluster count = " + obj1.clusterCount() + " clusters when using double hasing probing.");
            obj1.clearData();
            break;
        case 3:
            System.out.println("Load factor 0.7:");
            number = new int[70];
            for (int i = 0; i < 70; i++) {
                number[i] = (int) (Math.random() * 1000) + 1;
            }
            System.out.println("Linear probing.");
            for (int i : number) {
                obj1.insertLinear(i);
            }
            System.out
                    .println("Done.\nCluster count = " + obj1.clusterCount() + " clusters when using linear probing.");
            obj1.clearData();
            System.out.println("Quadratic probing.");
            for (int i : number) {
                obj1.insertQuadratic(i);
            }
            System.out.println(
                    "Done.\nCluster count = " + obj1.clusterCount() + " clusters when using quadratic probing.");
            obj1.clearData();
            System.out.println("Double hashing.");
            for (int i : number) {
                obj1.insertDoubleHashing(i);
            }
            System.out.println(
                    "Done.\nCluster count = " + obj1.clusterCount() + " clusters when using double hasing probing.");
            obj1.clearData();
            break;
        case 4:
            System.out.println("Load factor 0.9:");
            number = new int[91];
            for (int i = 0; i < 91; i++) {
                number[i] = (int) (Math.random() * 1000) + 1;
            }
            System.out.println("Linear probing.");
            for (int i : number) {
                obj1.insertLinear(i);
            }
            System.out
                    .println("Done.\nCluster count = " + obj1.clusterCount() + " clusters when using linear probing.");
            obj1.clearData();
            System.out.println("Quadratic probing.");
            for (int i : number) {
                obj1.insertQuadratic(i);
            }
            System.out.println(
                    "Done.\nCluster count = " + obj1.clusterCount() + " clusters when using quadratic probing.");
            obj1.clearData();
            System.out.println("Double hashing.");
            for (int i : number) {
                obj1.insertDoubleHashing(i);
            }
            System.out.println(
                    "Done.\nCluster count = " + obj1.clusterCount() + " clusters when using double hashing probing.");
            obj1.clearData();
            break;
        }
        sc.close();
    }
}