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

    public int clusterCount(int a) {
        if(a == arraySize-1)
            return 0;
        int counter = a;
        int cluster = 0;
        while(arrayData[counter++] != -1 && counter < arraySize){
        }
        cluster++;
        return(cluster + clusterCount(counter));
    }
}