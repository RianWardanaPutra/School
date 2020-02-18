import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Hash {
	private int[] arrayData;
	private int maxSize;
	private int currentSize;
	private int prime;
	private double probes = 0;
	public Queue<Integer> queueList = new LinkedList<>();
	//private int queueSize = 0;

	public Hash(int size, int load) {
		this.maxSize = size;
		this.currentSize = 0;
		arrayData = new int[maxSize];
		for (int i = 0; i < maxSize; i++) {
			this.arrayData[i] = 0;
		}

		for (int p = load; p < 100; p += 2) {
			if (p % 2 == 0) {
				p++;
			}
			if (isPrime(p)) {
				//System.out.print("\n p = " + p);
				prime = p;
				break;
			}
		}
		//System.out.println("hash created");
	}

	public int hashMethod(int key) {
		return (key % prime);
	}

	public boolean isFull() {
		return (currentSize == maxSize);
	}

	public void insert(int key) {
		if (isFull()) {
			System.out.println("Array is full!");
			return;
		}
		int index = hashMethod(key);
		if (arrayData[index] == 0) {
			arrayData[index] = key;
			currentSize++;
            //probes++;
		} else {
			queueList.add(key);
			//queueSize++;
		}
	}

	public void insertRestofData(int key) {
		if (isFull()) {
			System.out.println("Array is full!");
			return;
		}
		int index = hashMethod(key);
		while (arrayData[index] != 0) {
			index++;
			probes++;
			//System.out.println("probing");
			if (index >= maxSize) {
				index %= maxSize;
			}
		}
		arrayData[index] = key;
	}

	public double avgProbing() {
		double avg = 0;
		avg = probes / currentSize;
		return avg;
	}

	public boolean search(int key) {
		int index = hashMethod(key);
		int counter = 0;
		if (arrayData[index] == key) {
			return true;
		} else {
			while (arrayData[index] != key && arrayData[index] != 0) {
				index++;
				counter++;
				if (index >= maxSize) {
					index %= maxSize;
				}
				if (counter >= maxSize) {
					return false;
				}
			}
			if (arrayData[index] == key) {
				return true;
			} else {
				return false;
			}
		}
	}

	public boolean isPrime(int num) {
		if (num % 2 == 0 || num % 3 == 0) {
			return false;
		}
		for (int i = 5; i <= Math.sqrt(num); i += 6) {
			if (num % i == 0 || num % (i + 2) == 0) {
				return false;
			}
		}
		return true;
	}

	public void printData() {
		System.out.print("Data: ");
		for (int i : arrayData) {
			System.out.print(i + "-> ");
		}
	}
}

class Driver {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("~~Hashing~~");
		System.out.print("\nInsert value of table size: ");
		int value = sc.nextInt();
		System.out.print("\nInput number of random key that you would like to generate: ");
		int randomSize = sc.nextInt();
		while (randomSize >= value) {
			System.out.println("The number cannot exceeds the max size of hash table!\nInsert number: ");
			randomSize = sc.nextInt();
		}
		Hash obj = new Hash(value, randomSize);

		int[] randomNumber = new int[randomSize];
		for (int i = 0; i < randomSize; i++) {
			randomNumber[i] = (int) (Math.random() * 100) + 1;
		}
		for (int i : randomNumber) {
			obj.insert(i);
			//System.out.println("inserting numbers");
		}
		for (int left : obj.queueList) {
			//System.out.println("inserting left numbers");
			obj.insertRestofData(left);
		}
		int menu = 0;
		while (true) {
			System.out.println("\n\nMenu:\n[1] Search for data\n[2] Average probing\n[3] Print data\n[4] Exit");
			menu = sc.nextInt();
			switch (menu) {
			case 1:
				System.out.print("\nInsert key to be searched: ");
				int searchKey = sc.nextInt();
				boolean found = obj.search(searchKey);
				if (found) {
					System.out.println("Key " + searchKey + " found!");
				} else {
					System.out.println("Key " + searchKey + " not found.");
				}
				break;
			case 2:
				double averageProbe = obj.avgProbing();
				System.out.println("Count average probing.\n\nAverage probing: " + averageProbe);
				break;
			case 3:
				System.out.println("Hash table data: ");
				obj.printData();
				break;
			default:
				System.out.println("Thank you. Exiting...");
				sc.close();
				return;
			}
		}
	}
}
