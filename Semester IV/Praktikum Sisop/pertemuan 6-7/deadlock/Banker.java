public class Banker {

    public static void main(String[] args) {
        Banker bank = new Banker();

        bank.calculateNeed();

        bank.isSafe();
    }

    int n_process = 4;
    int n_res = 2;
    int[] process;
    int[][] needs;
    int[] resource;
    int[][] alloc;
    int[][] max;
    int[] safeSequence = new int[n_process];

    public Banker() {

        // PROCESS
        process = new int[n_process];

        // PROCESS NEEDS
        needs = new int[n_process][n_res];

        // max available resource
        resource = new int[] { 9, 6 };
        System.out.println("Available resource: ");
        System.out.println(resource[0] + " " + resource[1]);

        // allocated
        alloc = new int[][] { { 2, 1 }, // P0
                { 1, 0 }, // P1
                { 3, 2 }, // P2
                { 0, 1 } }; // P3

        // resource required per process
        max = new int[][] { { 6, 5 }, // P0
                { 7, 4 }, // P1
                { 5, 4 }, // P2
                { 4, 5 } }; // P3

        System.out.println();
        System.out.println("Allocated res:");
        for (int a = 0; a < n_process; a++) {
            System.out.print("P" + a + ": ");
            for (int b = 0; b < n_res; b++) {
                System.out.print(alloc[a][b] + " ");
            }
            System.out.println();
        }
        System.out.println();

        System.out.println("Resource needed for process to run and terminate:");
        for (int a = 0; a < n_process; a++) {
            System.out.print("P" + a + ": ");
            for (int b = 0; b < n_res; b++) {
                System.out.print(max[a][b] + " ");
            }
            System.out.println();
        }
        System.out.println();

    }

    void isSafe() {
        int count = 0;

        // visited array to find the already allocated process
        boolean[] visited = new boolean[n_process];
        for (int i = 0; i < n_process; i++) {
            visited[i] = false;
        }

        int[] sum = new int[n_res];
        for (int a = 0; a < n_res; a++) {
            for (int b = 0; b < n_process; b++) {
                sum[a] += alloc[b][a];
            }
        }
        
        // array to store copy of available resources
        System.out.println("Available resource after allocated: ");
        int[] work = new int[n_res];
        for (int i = 0; i < n_res; i++) {
            work[i] = resource[i] - sum[i];
            System.out.print(work[i] + " ");
        }
        System.out.println();
        System.out.println();

        while (count < n_process) {
            boolean flag = false;
            for (int i = 0; i < n_process; i++) {
                System.out.println("Checking P" + i);
                boolean a = false, b = false;
                if (visited[i] == false) {
                    int j;
                    for (j = 0; j < n_res; j++) {
                        System.out.println("Needs: " + needs[i][j] + ", available: " + work[j]);
                        if (needs[i][j] <= work[j]){
                            if(j==0) a = true;
                            else b = true;
                        }
                    }
                    
                    // If all resource are ready to be given to process
                    // run the process
                    if (a == true && b == true){
                        System.out.println("Satisfied!\n");
                        safeSequence[count++] = i;
                        visited[i] = true;
                        flag = true;
                        for(j = 0; j < n_res; j++) {
                            work[j] += alloc[i][j];
                        }
                    }
                    if (a == false || b == false) System.out.println("Skipping, for now\n");
                }
            }
            if (flag == false) break;
        }

        if (count < n_process) {
            System.out.println("The System is unsafe!");
        } else {

            System.out.println("\n\nFollowing is the Safe sequence: ");
            for (int i = 0; i < n_process; i++) {
                System.out.print("P" + safeSequence[i]);
                if (i != n_process - 1)
                    System.out.print(" -> ");
            }
        }
    }

    void calculateNeed() {
        System.out.println("Additional resource needed:");
        for (int i = 0; i < n_process; i++) {
            System.out.print("P" + i + ": ");
            for (int j = 0; j < n_res; j++) {
                needs[i][j] = max[i][j] - alloc[i][j];
                System.out.print(needs[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }
}
