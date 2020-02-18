import java.lang.reflect.Array;
import java.util.Random;
import java.util.Scanner;

/* renamed from: TugasGraph */
class TugasGraph {
    static final int INF = 99999;
    int V;

    public static void main(String[] Args) {
        /*
         * TugasGraph.printSlow("Halo..."); TugasGraph.
         * printSlow("Namaku Kyon, aku akan membantumu mengerjakan tugas terakhir\nPak Janoe tercinta :)"
         * ); TugasGraph.
         * printSlow("Task nya agak berat, jadi sebelum mulai di benchmark doeloe ya");
         * System.out.
         * print("\nPreparing benchmark test with Lucas Lehmer algorithm...\nStarting benchmark"
         * ); TugasGraph.fakeLoading(); System.out.println();
         * TugasGraph.printSlow("Wah, PC mu cupu sekali :("); TugasGraph.
         * printSlow("Tapi tak apa, kita coba test run dulu ya dengan jumlah vertex 10"
         * ); TugasGraph tugasGraph = new TugasGraph(10, true);
         * TugasGraph.printSlow("Wah, kelihatannya benar"); TugasGraph.
         * printSlow("Tapi aku masih ragu apakah CPU ini kuat, menurutmu bagaimana?");
         * System.out.println("1. Jalankan Dijsktra & Floyd");
         * System.out.println("2. Lihat source code saja"); Scanner scanner = new
         * Scanner(System.in); if (scanner.nextInt() == 2) {
         * TugasGraph.printSlow("Untuk melihat source code ku ada dua cara yaitu:");
         * TugasGraph.printSlow("A. Melakukan dekompilasi (decompile)");
         * TugasGraph.printSlow("B. Menjawab salah satu pertanyaan di bawah ini");
         * TugasGraph.printSlow(
         * "Namun, syaratnya adalah orang yang menjawab tidak boleh yang namanya ada di pertanyaan."
         * ); System.out.println("Pertanyaan :");
         * System.out.println("1.Siapa nama cici nya Hashfi ? (Salah satu)");
         * System.out.println("2.Siapa nama bebebnya Rian yg di filsafat ?");
         * System.out.
         * println("3.Berapa tebal maksimum kumis Arda semester kemarin ? (cm)");
         * System.out.println("4.Jam berapa klinik TongFang buka ?");
         * System.out.println("5.Siapa orang paling pedo di Ilkom-B ?"); System.out.
         * println("6.Berapa kali saya titip KTM ke Raven tapi dia malah ketiduran ?");
         * System.out.println("7.Siapa waifu Fadhlan ?");
         * System.out.println("8.Berapa maks shutter speed kamera Rafel ?");
         * System.out.println("9.Pohon jenis apa yang mecahin kaca mobil Acong ?");
         * System.out
         * .println("10.Berapa harga pijat plus plus yang ditawarkan ke Richie di depan stasiun/Hotel Neo ?"
         * ); System.out.
         * println("11.Lebih sering bolos saya, Raven, atau Naufan ? (di kertas)");
         * System.out.println("12.Berapa jumlah dakimakura Ferdi ?");
         * System.out.println("13.Berapa sisa credit Azure yang dimiliki Adhit ?");
         * System.out.println("14.Siapa nama mantan Pi'i ?");
         * System.out.println("15.Siapa nama anak Pak Shippuden ?"); scanner.nextLine();
         * while (true) { System.out.println("Pilih pertanyaan nomor : ");
         * scanner.nextLine(); System.out.println("Jawaban :"); scanner.nextLine();
         * TugasGraph.printSlow("Jawaban salah"); } } else {
         */
        System.out.println("Memulai task...");
        TugasGraph tugasGraph2 = new TugasGraph(1000, false);
        tugasGraph2 = new TugasGraph(1000, true);
        tugasGraph2 = new TugasGraph(10000, false);
        tugasGraph2 = new TugasGraph(10000, true);
        tugasGraph2 = new TugasGraph(20000, false);
        tugasGraph2 = new TugasGraph(20000, true);
        tugasGraph2 = new TugasGraph(50000, false);
        tugasGraph2 = new TugasGraph(50000, true);
        tugasGraph2 = new TugasGraph(100000, false);
        tugasGraph2 = new TugasGraph(100000, true);
        // scanner.close();
    }

    // }

    public TugasGraph(int i, boolean z) {
        this.V = i;
        int[][] generateGraph = generateGraph(z);
        long currentTimeMillis = System.currentTimeMillis();
        dijkstra(generateGraph, 0);
        System.out.println("Dijkstra 0 " + i + (z ? " Edge lengkap " : " Edge setengah ")
                + (System.currentTimeMillis() - currentTimeMillis) + " ms");
        currentTimeMillis = System.currentTimeMillis();
        for (int i2 = 0; i2 < i; i2++) {
            dijkstra(generateGraph, i2);
        }
        System.out.println("Dijkstra n " + i + (z ? " Edge lengkap " : " Edge setengah ")
                + (System.currentTimeMillis() - currentTimeMillis) + " ms");
        currentTimeMillis = System.currentTimeMillis();
        floydWarshall(generateGraph);
        System.out.println("Floyd " + i + (z ? " Edge lengkap " : " Edge setengah ")
                + (System.currentTimeMillis() - currentTimeMillis) + " ms");
    }

    /* Access modifiers changed, original: 0000 */
    public int[][] generateGraph(boolean z) {
        int[][] iArr = (int[][]) Array.newInstance(Integer.TYPE, new int[] { this.V, this.V });
        Random random = new Random();
        int i;
        int i2;
        if (z) {
            for (i = 0; i < this.V; i++) {
                for (i2 = i; i2 < this.V; i2++) {
                    if (i == i2) {
                        iArr[i][i2] = 0;
                    } else {
                        iArr[i][i2] = random.nextInt(999) + 1;
                        iArr[i2][i] = iArr[i][i2];
                    }
                }
            }
        } else {
            int i3 = (this.V * (this.V - 1)) / 4;
            i2 = 0;
            while (i2 < i3) {
                i = 0;
                while (i < this.V) {
                    int i4 = i;
                    while (i4 < this.V) {
                        if (i == i4) {
                            iArr[i][i4] = 0;
                        } else {
                            if (iArr[i][i4] == 0) {
                                iArr[i][i4] = INF;
                                iArr[i4][i] = iArr[i][i4];
                            }
                            if (random.nextBoolean() && iArr[i][i4] == INF && i2 < i3) {
                                iArr[i][i4] = random.nextInt(999) + 1;
                                iArr[i4][i] = iArr[i][i4];
                                i2++;
                            }
                        }
                        i4++;
                    }
                    i++;
                }
            }
        }
        return iArr;
    }

    /* Access modifiers changed, original: 0000 */
    public int minDistance(int[] iArr, Boolean[] boolArr) {
        int i = INF;
        int i2 = -1;
        int i3 = 0;
        while (i3 < this.V) {
            if (!boolArr[i3].booleanValue() && iArr[i3] <= i) {
                i = iArr[i3];
                i2 = i3;
            }
            i3++;
        }
        return i2;
    }

    /* Access modifiers changed, original: 0000 */
    public void dijkstra(int[][] iArr, int i) {
        int i2;
        int[] iArr2 = new int[this.V];
        Boolean[] boolArr = new Boolean[this.V];
        for (i2 = 0; i2 < this.V; i2++) {
            iArr2[i2] = INF;
            boolArr[i2] = Boolean.valueOf(false);
        }
        iArr2[i] = 0;
        for (i2 = 0; i2 < this.V - 1; i2++) {
            int minDistance = minDistance(iArr2, boolArr);
            boolArr[minDistance] = Boolean.valueOf(true);
            int i3 = 0;
            while (i3 < this.V) {
                if (!(boolArr[i3].booleanValue() || iArr[minDistance][i3] == 0 || iArr[minDistance][i3] == INF
                        || iArr2[minDistance] == INF || iArr2[minDistance] + iArr[minDistance][i3] >= iArr2[i3])) {
                    iArr2[i3] = iArr2[minDistance] + iArr[minDistance][i3];
                }
                i3++;
            }
        }
        if (this.V < 100) {
            printSolution(iArr2, this.V);
        }
    }

    /* Access modifiers changed, original: 0000 */
    public void printSolution(int[] iArr, int i) {
        System.out.println("Vertex\t\tDistance from Source");
        for (int i2 = 0; i2 < this.V; i2++) {
            System.out.println(i2 + "\t\t" + (iArr[i2] == INF ? "INF" : Integer.valueOf(iArr[i2])));
        }
    }

    /* Access modifiers changed, original: 0000 */
    public void floydWarshall(int[][] iArr) {
        int i;
        int i2;
        int[][] iArr2 = (int[][]) Array.newInstance(Integer.TYPE, new int[] { this.V, this.V });
        for (i = 0; i < this.V; i++) {
            for (i2 = 0; i2 < this.V; i2++) {
                iArr2[i][i2] = iArr[i][i2];
            }
        }
        for (i = 0; i < this.V; i++) {
            for (i2 = 0; i2 < this.V; i2++) {
                for (int i3 = 0; i3 < this.V; i3++) {
                    if (iArr2[i2][i] + iArr2[i][i3] < iArr2[i2][i3]) {
                        iArr2[i2][i3] = iArr2[i2][i] + iArr2[i][i3];
                    }
                }
            }
        }
        if (this.V < 100) {
            printSolution(iArr2);
        }
    }

    /* Access modifiers changed, original: 0000 */
    public void printSolution(int[][] iArr) {
        System.out.println("Matriks jarak terpendek antara dua vertex");
        for (int i = 0; i < this.V; i++) {
            for (int i2 = 0; i2 < this.V; i2++) {
                if (iArr[i][i2] == INF) {
                    System.out.print("INF ");
                } else {
                    System.out.print(iArr[i][i2] + "\t");
                }
            }
            System.out.println();
        }
    }

    /*
     * private static void printSlow(String str) { Random random = new Random(); for
     * (int i = 0; i < str.length(); i++) { try { Thread.sleep((long)
     * random.nextInt(250)); } catch (Exception e) { }
     * System.out.print(str.charAt(i)); } System.out.println(); }
     * 
     * private static void fakeLoading() { System.out.println(); Random random = new
     * Random(); System.out.print("   "); for (int i = 0; i <= 100; i++) {
     * System.out.print("\b\b\b"); if (i < 10) { System.out.print("0"); }
     * System.out.print(i + "%"); try { Thread.sleep((long) random.nextInt(300)); }
     * catch (Exception e) { } } }
     */
}