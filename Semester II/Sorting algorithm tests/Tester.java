import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;
import java.util.concurrent.TimeUnit;

class Tester {
    int partition(int arr[], int low, int high) {
        int pivot = arr[low+(high-low)/2];
        int left = low-1;
        int right = high+1;

        while (true) {
            while (arr[++left] < pivot);
            while (arr[--right] > pivot);

            if (left < right) {
                int tmp = arr[left];
                arr[left] = arr[right];
                arr[right] = tmp;
            } else {
                return right;
            }
        }
    }

    /*
     * The main function that implements QuickSort() arr[] --> Array to be sorted,
     * low --> Starting index, high --> Ending index
     */
    void quickSort(int arr[], int low, int high) {
        while (low < high) {
            int pi = partition(arr, low, high);
            if (pi - low <= high - (pi + 1)) {
                quickSort(arr, low, pi);
                low = pi + 1;
            } else {
                quickSort(arr, pi + 1, high);
                high = pi;
            }
        }
    }

    public void sort(int[] arr) {
        int[] aux = new int[arr.length];
        mergeSort(arr, aux, 0, arr.length - 1);
    }

    public void mergeSort(int[] arr, int[] aux, int low, int high) {
        if (low < high) {
            int mid = low + (high - low) / 2;
            mergeSort(arr, aux, low, mid);
            mergeSort(arr, aux, mid + 1, high);
            if (arr[mid + 1] >= arr[mid]) {
                return;
            }
            merge(arr, aux, low, mid, high);
        }
    }

    public void merge(int[] arr, int[] aux, int low, int mid, int high) {
        for (int k = low; k <= high; k++) {
            aux[k] = arr[k];
        }

        int left = low, right = mid + 1;
        for (int k = low; k <= high; k++) {
            if (left > mid)
                arr[k] = aux[right++];
            else if (right > high)
                arr[k] = aux[left++];
            else if (aux[right] < aux[left])
                arr[k] = aux[right++];
            else
                arr[k] = aux[left++];
        }
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

    public static void main(String[] args) throws IOException, FileNotFoundException, StackOverflowError {
        Scanner sc = new Scanner(System.in);
        int menu;
        System.out.println("Masukkan angka pada nama file: ");
        String namaFile = sc.nextLine();
        File file = new File("randomNumber" + namaFile + ".txt");
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
            obj1.sort(arrayAngka);
            long endTime = System.nanoTime();
            long elapsedTime = endTime - startTime;
            long minutes = TimeUnit.NANOSECONDS.toMinutes(elapsedTime);
            long seconds = TimeUnit.NANOSECONDS.toSeconds(elapsedTime) - TimeUnit.MINUTES.toSeconds(minutes);
            long miliSeconds = TimeUnit.NANOSECONDS.toMillis(elapsedTime) - (TimeUnit.MINUTES.toMillis(minutes) + TimeUnit.SECONDS.toMillis(seconds));
            long nanoSeconds = elapsedTime - (TimeUnit.MINUTES.toNanos(minutes) + TimeUnit.SECONDS.toNanos(seconds) + TimeUnit.MILLISECONDS.toNanos(miliSeconds));
            System.out.println("elapsed time (nanoseconds): " + elapsedTime);
            System.out.println("elapsed time: " + minutes + "m " + seconds + "s " + miliSeconds + "ms " + nanoSeconds + "ns.");
            // printer(randomArr);
            break;
        case 2:

            Tester obj2 = new Tester();
            System.out.println("Press any key to start");
            sc.next();
            long startTime2 = System.nanoTime();

            obj2.quickSort(arrayAngka, 0, arrayAngka.length - 1);
            long endTime2 = System.nanoTime();
            long elapsedTime2 = endTime2 - startTime2;
            long minutes2 = TimeUnit.NANOSECONDS.toMinutes(elapsedTime2);
            long seconds2 = TimeUnit.NANOSECONDS.toSeconds(elapsedTime2) - TimeUnit.MINUTES.toSeconds(minutes2);
            long miliSeconds2 = TimeUnit.NANOSECONDS.toMillis(elapsedTime2) - (TimeUnit.MINUTES.toMillis(minutes2) + TimeUnit.SECONDS.toMillis(seconds2));
            long nanoSeconds2 = elapsedTime2 - (TimeUnit.MINUTES.toNanos(minutes2) + TimeUnit.SECONDS.toNanos(seconds2) + TimeUnit.MILLISECONDS.toNanos(miliSeconds2));
            System.out.println("elapsed time (nanoseconds): " + elapsedTime2);
            System.out.println("elapsed time: " + minutes2 + "m " + seconds2 + "s " + miliSeconds2 + "ms " + nanoSeconds2 + "ns.");
            break;
        case 3:

            Tester obj3 = new Tester();
            System.out.println("Press any key to start");
            sc.next();
            long startTime3 = System.nanoTime();
            obj3.heapSort(arrayAngka);
            long endTime3 = System.nanoTime();
            long elapsedTime3 = endTime3 - startTime3;
            long minutes3 = TimeUnit.NANOSECONDS.toMinutes(elapsedTime3);
            long seconds3 = TimeUnit.NANOSECONDS.toSeconds(elapsedTime3) - TimeUnit.MINUTES.toSeconds(minutes3);
            long miliSeconds3 = TimeUnit.NANOSECONDS.toMillis(elapsedTime3) - (TimeUnit.MINUTES.toMillis(minutes3) + TimeUnit.SECONDS.toMillis(seconds3));
            long nanoSeconds3 = elapsedTime3 - (TimeUnit.MINUTES.toNanos(minutes3) + TimeUnit.SECONDS.toNanos(seconds3) + TimeUnit.MILLISECONDS.toNanos(miliSeconds3));
            System.out.println("elapsed time (nanoseconds): " + elapsedTime3);
            System.out.println("elapsed time: " + minutes3 + "m " + seconds3 + "s " + miliSeconds3 + "ms " + nanoSeconds3 + "ns.");
            break;
        default:
            break;
        }
        System.out.println("Thank you!");
        sc.close();
    }
}
