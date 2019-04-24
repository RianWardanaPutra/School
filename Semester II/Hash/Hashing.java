class HashTable {
    int key;
    int value;
    public HashTable (int key, int value) {
        this.key = key;
        this.value = value;
    }
}

class Hashing {
    int arraySize;
    int currentSize;
    HashTable[] arrayData;

    public Hashing(int size) {
        currentSize = 0;
        this.arraySize = size;
        arrayData = new HashTable[size];
        //for (HashTable i : arrayData) {
        //    i = null;
        //}
    }

    public boolean isTableFull () {
        return (currentSize == arraySize);
    }
    
    public int modMethod (int key, int mod) {
        return (key % mod);
    }

    public void insertQuadratic (int key, int value) {
        int index = modMethod(key, arraySize);
        int i = 1;
        if (isTableFull()) {
            System.out.println("Array is full!");
            return;
        } else {
            while (arrayData[index] != null) {
                index += i*i;
                if (index == arraySize) {
                    index = 0;
                } else if (index >= arraySize) {
                    index %= arraySize;
                }
                i++;
            }
            arrayData[index] = new HashTable(key, value);
            currentSize++;
        }
    }
}
    