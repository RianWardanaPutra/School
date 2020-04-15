/* Nama:        Fransiskus Rian Wardana Putra
 * NIM:         18/427592/PA/18552
 * Processor:   AMD FX-9830P
 * Java Ver.:   Java 13 OpenJDK
 * Text Editor: Visual Studio Code 
 */

// Class RunnableClass adalah class runnable yang kita gunakan
// untuk menjalankan thread karena untuk thread agar bisa
// berjalan memerlukan class runnable.
// Implements Runnable berarti class RunnableClass
// mengimplementasikan interface Runnable.
// Interface berisi susunan method yang harus ada 
// dalam suatu class, berbeda dengan extends class.

class RunnableClass implements Runnable {
    private Thread t;
    private String threadName;
    private String buffer;

    RunnableClass (String name, String bufferString) {
        threadName = name;
        buffer = bufferString;
    }

    public void run() {

        // Bagaimana thread saat dijalankan terdapat
        // dalam method run() milik Runnable

        System.out.println("Running " + threadName);
        try {
            for(int i = 0; i < 2; i++) {
                System.out.println("String: " + buffer + ", " + threadName + "\n");
                Thread.sleep(50);
            }

        // Exception handling

        } catch (InterruptedException e) {
            //TODO: handle exception
            System.out.println("Thread " + threadName + " interupted.");
        }
        System.out.println("Thread " + threadName + " exiting.");
    }

    // Method yang membuat instance Thread baru saat
    // objek class dibuat di program main.
    public void start() {
        System.out.println("Starting " + threadName);
        if (t == null) {
            t = new Thread(this, threadName);
            t.start();
        }
    }
    
}

public class Tugas4 {
    public static void main(String[] args) {

        // Pembuatan objek thread

        RunnableClass R1 = new RunnableClass("Thread-1",  
                "Fransiskus Rian Wardana Putra");
        
        // Memanggil method start(), yang akan membuat thread
        // dapat dijalankan
        
        R1.start();

        RunnableClass R2 = new RunnableClass("Thread-2", "18/427592/PA/18552");
        R2.start();

        RunnableClass R3 = new RunnableClass("Thread-3", "Ilkomp B Reguler");
        R3.start();

        RunnableClass R4 = new RunnableClass("Thread-4", "Praktikum Sistem Operasi A4");
        R4.start();
    }
}