import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

class Vertex {
    boolean isVisited;
    String label;

    public Vertex(String label) {
        this.label = label;
        this.isVisited = false;
    }
}

class Graph {
    private Vertex[] vertex;
    private int vMax;
    private int[][] adjMat;
    public int nV;

    private Queue<Integer> que = new LinkedList<>();
    private Stack<Integer> stack = new Stack<>();

    Graph(int vMax) {
        this.vMax = vMax;
        nv = 0;
        vertex = new Vertex[vMax];
        adjMat = new int[vMax][vMax];
    }

    public boolean isEmpty() {
        return this.nV == 0;
    }

    public boolean isFull() {
        return this.nV == this.vMax;
    }

    public void addVertex(String label) {
        if(!isFull()){
            vertex[nV] = new Vertex(label);
            nV++;
            return;
        } else {
            System.out.println("Graph is full!");
            return;
        }
    }

    public boolean addEdge(int src, int dest) {
        if(src < vMax && dest < vMax) {
            this.adjMat[src][dest] = 1;
            this.adjMat[dest][src] = 1;
            return true;
        }
        return false;
    }

    public void bfs() {
        
    }
}