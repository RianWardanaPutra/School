import java.util.Scanner;

class Graph {
    private int maxJumlah;
    private int counter = 0;
    String[] vertex;
    int[][] distance;
    Graph(int jumlah) {
        this.maxJumlah = jumlah;
        distance = new int[jumlah][jumlah];
        for (int i = 0; i < jumlah; i++) {
            for (int j = 0; j < jumlah; j++) {
                if (i != j) {
                    graph[i][j] = inf;
                    distance[i][j] = inf;
                } else {
                    graph[i][j] = 0;
                    distance[i][j] = 0;
                }
            }
        }
    }

    public void addVertex(String vert) {
        vertex[counter++] = vert;
    }
}

class TugasGraph {
    public static int n;
    public static int inf = 99999;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

    }
}