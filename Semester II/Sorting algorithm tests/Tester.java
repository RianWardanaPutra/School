import java.security.NoSuchAlgorithmException;
import java.security.NoSuchProviderException;
import java.security.SecureRandom;
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

    public static void swap(int a, int b) {
        int temp = a;
        a = b;
        b = temp;
    }

    public void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);

            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }

    public int partition(int[] arr, int low, int high) {
        int pivot = arr[low];
        int i = (low + 1);
        for (int j = low; j <= high; j++) {
            if (arr[j] <= pivot) {
                System.out.println(i);
                // swap(arr[i], arr[j]);
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                i++;
            }
        }
        // swap(arr[i+1], arr[high]);
        int temp = arr[i - 1];
        arr[i - 1] = arr[high];
        arr[high] = temp;
        return (i - 1);
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

    public static void main(String[] args) throws NoSuchAlgorithmException, NoSuchProviderException {
        Scanner sc = new Scanner(System.in);
        int menu;
    
        System.out.println("Menu:\n[1] Merge\n[2] Quick\n[3] Heap\n[4] Exit");
        menu = sc.nextInt();
        switch (menu) {
            case 1:
                int[] randomArr = new int[500000000];
                SecureRandom randomize = SecureRandom.getInstance("SHA1PRNG", "SUN");
                for(int itr = 0; itr < 500000000; itr++) {
                //    randomArr[itr] = (int) (Math.random() * 100000000 ) + 1;
                    randomArr[itr] = randomize.nextInt();
                }
                //printer(randomArr);
                Tester obj1 = new Tester();
                long startTime = System.nanoTime();
                obj1.mergeSort(randomArr, 0, (500000000-1));
                long endTime = System.nanoTime();
                long elapsedTime = endTime - startTime;
                System.out.println("elapsed time: " + elapsedTime);
                System.out.println("time in milis: " + TimeUnit.NANOSECONDS.toMillis(elapsedTime));
                System.out.println("time in seconds: " + TimeUnit.NANOSECONDS.toSeconds(elapsedTime));
                //printer(randomArr);
                break;
            case 2:
                int[] randomArr2 = new int[5];
                for(int itr = 0; itr < 5; itr++) {
                    randomArr2[itr] = (int) (Math.random() * 100) + 1;
                }
                printer(randomArr2);
                Tester obj2 = new Tester();
                long startTime2 = System.nanoTime();
                try{
                    obj2.quickSort(randomArr2, 0, 4);
                } catch (ArrayIndexOutOfBoundsException e) {
                    e.printStackTrace();
                }
                long endTime2 = System.nanoTime();
                long elapsedTime2 = endTime2 - startTime2;
                System.out.println("elapsed time: " + elapsedTime2);
                printer(randomArr2);
                break;
            case 3:
                int[] randomArr3 = new int[20];
                for(int itr = 0; itr < 20; itr++) {
                    randomArr3[itr] = (int) (Math.random() * 100) + 1;
                }
                printer(randomArr3);
                Tester obj3 = new Tester();
                long startTime3 = System.nanoTime();
                obj3.heapSort(randomArr3);
                long endTime3 = System.nanoTime();
                long elapsedTime3 = endTime3 - startTime3;
                System.out.println("elapsed time: " + elapsedTime3);
                printer(randomArr3);
                break;
            default:
                break;
        }
        
        sc.close();
    }
}