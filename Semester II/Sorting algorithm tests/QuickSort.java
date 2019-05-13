import java.util.Scanner;

class QuickSort {
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
            System.out.println("pi = " + pi + ", low = " + low + ", High = " + high);
            if (pi - low <= high - (pi + 1)) {
                quickSort(arr, low, pi);
                printer(arr);
                low = pi + 1;
            } else {
                quickSort(arr, pi + 1, high);
                printer(arr);
                high = pi;
            }
        }
    }

    public static void printer(int[] arr) {
        for (int i : arr) {
            System.out.print(i + " -> ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Masukkan jumlah array: ");
        int size = sc.nextInt();
        int[] array = new int[size];

        for(int i = 0; i < size; i++) {
            array[i] = (int) (Math.random()*100) + 1;
        }

        printer(array);
        QuickSort qs = new QuickSort();
        qs.quickSort(array, 0, size-1);
        printer(array);

        sc.close();
    }
}