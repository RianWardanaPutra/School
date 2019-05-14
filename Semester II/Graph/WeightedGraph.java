import java.util.ArrayList;
import java.lang.Comparable;

class Vertex {
    //private ArrayList<Edge> neighborhood;
    private String kota;
    private boolean isVisited;

    public Vertex(String label) {
        this.kota = label;
        //this.neighborhood = new ArrayList<>();
        this.isVisited = false;
    }
}

class WeightedGraph {
    private Vertex v[];
    private int vMax;
    private int[][] adjMat;
    public int nV;

    public Graph(int vMax) {
        this.vMax = vMax;
        nV = 0;
        v = new Vertex[vMax];
        adjMat = new int[vMax][vMax];
        for(int i = 0; i < vMax; i++) {
            for(int j = 0; j < vMax; j++) {
                adjMat[i][j] = 0;
            }
        }
    }

    public void addVertex(String label) {
        v[nV] = new Vertex(label);
        nV++;
    }

    public void addEdge(int source, int destination, int weight) {
        adjMat[source][destination] = weight;
        adjMat[destination][source] = weight;
    }

    int minDistance(int[] distance, boolean[] sptSet) {
        int min = Integer.MAX_VALUE, minIndex = -1;
        for (int v = 0; v < vMax; v++) {
            if(sptSet[v] == false && distance[v] <= min) {
                min = dist[v];
                minIndex = v;
            }
        }
        return minIndex;
    }

    void printSolution (int[] distance, int n) {
        System.out.println("Vertex distance from source");
        for(int i = 0; i < vMax; i++) {
            System.out.println(i + " tt " + distance[i]);
        }
    }

    void dijkstra(int src) {
        int[][] graph = adjMat;
        int[] distance = new int[vMax];
        boolean[] sptSet = new boolean[vMax];
        for (int i = 0; i < vMax; i++) {
            distance[i] = Integer.MAX_VALUE;
            sptSet[i] = false;
        }
        distance[src] = 0;
        for(int count = 0; count < vMax-1; count++) {
            int u = minDistance(distance, sptSet);
            sptSet[u] = true;
            for(int v = 0; v <vMax; v++) {
                if(!sptSet[v] && graph[u][v] != 0 && distance[u] != Integer.MAX_VALUE && distance[u] + graph[u][v] < distance[v]) {
                    distance[v] = distance[u] + graph[u][v];
                }
            }
        }
        printSolution(distance, vMax);
    }
}