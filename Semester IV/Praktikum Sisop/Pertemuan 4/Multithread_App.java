/* 
 * Nama: Fransiskus Rian Wardana Putra
 * NIM: 18/427592/PA/18552 
 * Processor: AMD FX-9830P
 * Java Ver.: Java 13 OpenJDK
 * Text Editor: Visual Studio Code 
 */

// Class RunnableDemo adalah class runnable yang kita gunakan
// untuk menjalankan thread karena untuk thread agar bisa
// berjalan memerlukan class runnable.
// Implements Runnable berarti class RunnableDemo
// mengimplementasikan interface Runnable.
// Interface berisi susunan method yang harus ada 
// dalam suatu class, berbeda dengan extends class.
class RunnableDemo implements Runnable {
    private Thread t;
    private String threadName;
    int a = 0;

    // Constructor dalam membuat runnable thread.
    RunnableDemo(String name) {
        threadName = name;
        System.out.println("Creating " + threadName);
    }


    // method run() merupakan aksi yang dijalankan
    // ketika thread berjalan. Apa yang ingin kita
    // lakukan pada thread berada pada method run().
    // kita tidak memanggil run(), tetapi yang kita 
    // panggil adalah method start() di bawah.
    @Override
    public void run() {
        // TODO Auto-generated method stub
        System.out.println("Running " + threadName);
        try {
            for (int i = 0; i < 2; i++) {
                a++;
                System.out.println("Nilai: " + a + ", " + threadName);
                Thread.sleep(50);
            }
        } catch (InterruptedException e) {
            System.out.println("Thread " + threadName + " interupted.");
        }
        System.out.println("Thread " + threadName + " exiting.");
    }

    // method start() digunakan untuk menjalankan thread.
    // di sini start() tidak memanggil run(), meskipun run()
    // akan berjalan ketika start() dipanggil, karena
    // secara default start() telah memanggil run() di background
    // ketika start() dipanggil
    public void start() {
        System.out.println("Starting " + threadName);

        // pengecekan agar tidak membuat thread baru 
        // di atas thread yang telah berjalan jika 
        // method start() terpanggil.
        if (t == null) {
            t = new Thread (this, threadName);
            t.start();
        }
    }
}

public class Multithread_App {
    public static void main(String[] args) {

        // Pembuatan thread
        RunnableDemo R1 = new RunnableDemo("Thread-1");

        // Thread dijalankan
        R1.start();

        RunnableDemo R2 = new RunnableDemo("Thread-2");
        R2.start();
    }
}