import java.util.Scanner;

class MergeSort {
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

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Input the size of array: ");
        int size = sc.nextInt();
        int[] array = new int[size];
        for (int i = 0; i < size; i++) {
            array[i] = (int) (Math.random() * 100) + 1;
        }

        System.out.println("Array before sort: ");

        for(int a : array)
            System.out.print(a + ", ");

        MergeSort obj1 = new MergeSort();
        obj1.sort(array);

        System.out.println("\nArray after sort: ");

        for(int a : array)
        System.out.print(a + ", ");
        sc.close();
    }
}