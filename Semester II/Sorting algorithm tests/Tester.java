import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;
import java.util.concurrent.TimeUnit;

class Tester {
    public void mergeSort(int[] arr, int l, int r) {
        if (l < r) {
            int m = l + (r - l) / 2;

            mergeSort(arr, l, m);
            mergeSort(arr, m + 1, r);

            merge(arr, l, m, r);
        }
    }

    public void merge(int[] arr, int left, int mid, int right) {
        int i, j, k;
        int total1 = mid - left + 1;
        int total2 = right - mid;

        int[] L = new int[total1];
        int[] R = new int[total2];

        for (i = 0; i < total1; i++)
            L[i] = arr[left + i];
        for (j = 0; j < total2; j++)
            R[j] = arr[mid + 1 + j];

        i = 0;
        j = 0;
        k = left;

        while (i < total1 && j < total2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            } else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }

        while (i < total1) {
            arr[k] = L[i];
            i++;
            k++;
        }

        while (j < total2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }

    public void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);

            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }

    public int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int tracker = (low - 1);
        for (int counter = low; counter < high; counter++) {
            if (arr[counter] <= pivot) {
                System.out.println(tracker);
                // swap(arr[i], arr[j]);
                tracker++;
                int temp = arr[tracker];
                arr[tracker] = arr[counter];
                arr[counter] = temp;
            }
        }
        // swap(arr[i+1], arr[high]);
        int temp = arr[tracker + 1];
        arr[tracker + 1] = arr[high];
        arr[high] = temp;
        return (tracker + 1);
    }

    public void heapSort(int[] arr) {
        int n = arr.length;
        for (int i = n / 2 - 1; i >= 0; i--) {
            heapify(arr, n, i);
        }

        for (int i = n - 1; i >= 0; i--) {
            // swap(arr[0], arr[i]);
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;
            heapify(arr, i, 0);
        }
    }

    public void heapify(int[] arr, int size, int i) {
        int largest = i;
        int left = 2 * i + 1;
        int right = left + 1;

        if (left < size && arr[left] > arr[largest])
            largest = left;

        if (right < size && arr[right] > arr[largest])
            largest = right;

        if (largest != i) {
            // swap(arr[i], arr[largest]);
            int temp = arr[i];
            arr[i] = arr[largest];
            arr[largest] = temp;
            heapify(arr, size, largest);
        }
    }

    public static void printer(int[] arr) {
        for (int i : arr) {
            System.out.print(i + " -> ");
        }
        System.out.println();
    }

    public static void main(String[] args) throws IOException, FileNotFoundException {
        Scanner sc = new Scanner(System.in);
        int menu;
        System.out.println("Masukkan nama file: ");
        String namaFile = sc.nextLine();
        File file = new File(namaFile);
        BufferedReader reader = new BufferedReader(new FileReader(file));
        if (reader != null) {
            System.out.println("File exists");
        }
        System.out.println("Masukkan jumlah data dalam file (misal 1000): ");
        int size = sc.nextInt();
        int[] arrayAngka = new int[size];
        System.out.println("Memasukkan data ke dalam array... ");
        for (int angka = 0; angka < size; angka++) {
            if (reader.readLine() != null) {
                arrayAngka[angka] = Integer.parseInt(reader.readLine());
            }
        }
        if (reader != null) {
            reader.close();
        }
        System.out.println("Menu:\n[1] Merge\n[2] Quick\n[3] Heap\n[4] Exit");
        menu = sc.nextInt();
        switch (menu) {
        case 1:
            // printer(randomArr);
            Tester obj1 = new Tester();
            System.out.println("Press any key to start");
            sc.next();
            long startTime = System.nanoTime();
            obj1.mergeSort(arrayAngka, 0, (size - 1));
            long endTime = System.nanoTime();
            long elapsedTime = endTime - startTime;
            System.out.println("elapsed time: " + elapsedTime);
            System.out.println("time in milis: " + TimeUnit.NANOSECONDS.toMillis(elapsedTime));
            System.out.println("time in seconds: " + TimeUnit.NANOSECONDS.toSeconds(elapsedTime));
            System.out.println("time in minutes: " + TimeUnit.NANOSECONDS.toMinutes(elapsedTime));
            // printer(randomArr);
            break;
        case 2:

            Tester obj2 = new Tester();
            System.out.println("Press any key to start");
            sc.next();
            long startTime2 = System.nanoTime();
            try {
                obj2.quickSort(arrayAngka, 0, size - 1);
            } catch (ArrayIndexOutOfBoundsException e) {
                e.printStackTrace();
            }
            long endTime2 = System.nanoTime();
            long elapsedTime2 = endTime2 - startTime2;
            System.out.println("elapsed time: " + elapsedTime2);
            System.out.println("time in milis: " + TimeUnit.NANOSECONDS.toMillis(elapsedTime2));
            System.out.println("time in seconds: " + TimeUnit.NANOSECONDS.toSeconds(elapsedTime2));
            System.out.println("time in minutes: " + TimeUnit.NANOSECONDS.toMinutes(elapsedTime2));
            break;
        case 3:

            Tester obj3 = new Tester();
            System.out.println("Press any key to start");
            sc.next();
            long startTime3 = System.nanoTime();
            obj3.heapSort(arrayAngka);
            long endTime3 = System.nanoTime();
            long elapsedTime3 = endTime3 - startTime3;
            System.out.println("elapsed time: " + elapsedTime3);
            System.out.println("time in milis: " + TimeUnit.NANOSECONDS.toMillis(elapsedTime3));
            System.out.println("time in seconds: " + TimeUnit.NANOSECONDS.toSeconds(elapsedTime3));
            System.out.println("time in minutes: " + TimeUnit.NANOSECONDS.toMinutes(elapsedTime3));
            break;
        default:
            break;
        }
        System.out.println("Thank you! \n*pant (exhausted)...");
        sc.close();
    }
}