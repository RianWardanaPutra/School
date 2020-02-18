import java.util.Scanner;
import java.util.Random;

class Graph {
  public static int n;
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    System.out.print("banyak vertek = ");
    n = input.nextInt();
    int i, j, k, c1 = 0, c2 = 0;
    int[][] G = new int[n][n];
    int[] L = new int[n];
    int[][] P = new int[n][n];
    Random r = new Random();
    for (i = 0; i < n; i++)
      for (j = i + 1; j < n; j++) {
        int rd = r.nextInt(1000) + 1;
        if (rd < 250) {
          G[i][j] = rd;
          c1++;
        } else {
          G[i][j] = 9999;
          c2++;
        }
        G[j][i] = G[i][j];
      }
    System.out.println("Matrik Distance : " + c1 + "  " + c2);
    for (i = 0; i < n; i++) {
      L[i] = 0;
      System.out.println();
      for (j = 0; j < n; j++) {
        P[i][j] = 0;
        System.out.print(G[i][j]);
        System.out.print("\t");
      }
    }
    for (k = 0; k < n; k++) // floyd
      for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
          if (i != k && j != k && i != j)
            if (G[i][j] > G[i][k] + G[k][j]) {
              G[i][j] = G[i][k] + G[k][j];
              P[i][j] = k;
            }
    System.out.println();
    System.out.println("Matrik Shortestdistance :");
    for (i = 0; i < n; i++) {
      System.out.println();
      for (j = 0; j < n; j++) {
        System.out.print(G[i][j]);
        System.out.print("\t");
      }
    }
    System.out.println();
    System.out.println("Matrik Sebelum :");
    for (i = 0; i < n; i++) {
      System.out.println();
      for (j = 0; j < n; j++) {
        System.out.print(P[i][j]);
        System.out.print("\t");
      }
    }
    System.out.println();
    System.out.print("vertek awal = ");
    int a = input.nextInt();
    System.out.print("vertek akhir = ");
    int b = input.nextInt();

    i = n - 2;
    L[n - 1] = b;
    do {
      L[i] = P[a][b];
      b = P[a][b];
      i--;
    } while (b != 0);
    L[i] = a;
    System.out.println("Jalur terpendek :");

    for (i = 0; i < n; i++) {
      if (L[i] != 0) {
        System.out.print(L[i]);
        if (i != n - 1)
          System.out.print("-");
      }
    }
    System.out.println();
    input.close();
  }
}

