import java.util.Scanner;

class LinkedHash {
    private String key;
    private int value;

    public LinkedHash next;

    public LinkedHash(String key, int value) {
        this.key = key;
        this.value = value;
        this.next = null;
    }

    public String getKey() {
        return this.key;
    }

    public int getValue() {
        return this.value;
    }
}

class NewHashing {
    LinkedHash[] hashTable;
    private int maxSize;
    private int currentSize;

    public NewHashing(int max) {
        this.maxSize = max;
        this.currentSize = 0;
        hashTable = new LinkedHash[max];
        for (int i = 0; i < maxSize; i++) {
            hashTable[i] = null;
        }
    }

    public boolean isFull() {
        return (currentSize == maxSize);
    }

    public void insert(String key, int value) {
        if (isFull) {
            System.out.println("Hash table is full! Cannot insert new map anymore!");
            return;
        } else {
            int position = hashMethod(key);
            LinkedHash temp = new LinkedHash(key, value);
            if (hashTable[position] == null) {
                hashTable[position] = temp;
            } else if (hashTable[position] != null) {
                LinkedHash current = hashTable[position];
                while (current.next != null) {
                    current = current.next;
                }
                current.next = temp;
            }
            currentSize++;
        }
    }

    public int hashMethod(String x) {
        int hashValue = x.hashCode();
        hashValue %= maxSize;
        if (hashValue < 0) {
            hashValue += maxSize;
        }
        return hashValue;
    }

    public LinkedHash search(String key) {
        int position = hashMethod(key);
        if (hashTable[position].getKey() == key) {
            return hashTable[position];
        } else {
            LinkedHash current = hashTable[position];
            while (current.getKey() != key && current.next != null) {
                current = current.next;
            }
            if (current.getKey() == key) {
                return current;
            } else {
                return null;
            }
        }
    }

    public LinkedHash removeEntity(String key) {
        int position = hashMethod(key);
        if (hashTable[position].getKey() == key) {
            LinkedHash temp = hashTable[position];
            if (hashTable[position].next == null) {
                hashTable[position] = null;
            } else if (hashTable[position].next != null) {
                hashTable[position] = hashTable[position].next;
            }
            currentSize--;
            return temp;
        } else {
            LinkedHash current = hashTable[position];
            while (current.next.getKey() != key && current.next.next != null) {
                current = current.next;
            }
            if (current.next.getKey() == key) {
                LinkedHash temp = current.next;
                current.next = current.next.next;
                currentSize--;
                return temp;
            } else {
                return null;
            }
        }
    }
}

class NewHashDriver {
    Scanner sc = new Scanner(System.in);
    int menu = sc.nextInt();

}