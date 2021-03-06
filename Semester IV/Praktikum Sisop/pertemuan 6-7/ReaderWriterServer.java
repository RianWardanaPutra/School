// Class utama yang menjalankan keseluruhan program
// di class ini tidak diletakkan satupun method.
public class ReaderWriterServer {

    private static int NUM_OF_READERS = 3;
    private static int NUM_OF_WRITERS = 2;

    public static void main(String[] args) {

        // Inisialisasi data, terdapat array Reader dan Writer 
        // dengan jumlah yang telah ditentukan.
        Database server = new Database();
        Reader[] readerArray = new Reader[NUM_OF_READERS];
        Writer[] writerArray = new Writer[NUM_OF_WRITERS];

        // Thread reader dan writer dijalankan secara berurutan.
        // Di sini belum terlihat prioritas reader atau writer.
        for (int i = 0; i < NUM_OF_READERS; i++) {
            readerArray[i] = new Reader(i, server);
            readerArray[i].start();
        }
        for (int i = 0; i < NUM_OF_WRITERS; i++) {
            writerArray[i] = new Writer(i, server);
            writerArray[i].start();
        }
    }
}

// Class Reader
class Reader extends Thread {

    private Database server;
    private int readerNum;

    public Reader(int r, Database db) {
        readerNum = r;
        server = db;
    }

    // Proses dari reader cycle.
    public void run() {

        int c;

        while (true) {
            Database.tunggu();
            System.out.println("Reader " + readerNum + " wants to read.");
            c = server.mulaiBaca();
            System.out.println("Reader " + readerNum + " is reading. Reader count = " + c);
            Database.tunggu();
            System.out.println("Reader " + readerNum + " is done reading.");
            c = server.selesaiBaca();
        }
    }
}

class Writer extends Thread {

    private Database server;
    private int writerNum;

    public Writer(int w, Database db) {
        writerNum = w;
        server = db;
    }

    // Proses dari writer cycle.
    public void run() {

        while (true) {
            System.out.println("Writer " + writerNum + " is sleeping.");
            Database.tunggu();
            System.out.println("Writer " + writerNum + " wants to write.");
            server.mulaiTulis();
            System.out.println("Writer " + writerNum + " is writing.");
            Database.tunggu();
            System.out.println("Writer " + writerNum + " is done writing.");
            server.selesaiTulis();
        }
    }
}

// Class semaphore untuk mengontrol state thread
final class Semaphore {

    private int value;

    public Semaphore() { value = 0; }

    public Semaphore(int v) { value = v; }

    public synchronized void tutup() {

        while (value <= 0) {

            // jika value semaphore kurang dari 1, 
            // maka thread akan masuk waiting state.
            try {
                wait();
            } catch (InterruptedException e) {}
        }
        value--;
    }

    // saat buka() dipanggil, maka value akan ditambah
    // notify digunakan untuk memberitau thread
    // monitor agar thread berlanjut dan tidak lagi dalam waiting state.
    public synchronized void buka() {
        ++value; 
        notify();
    }

}

class Database {

    // Digunakan 2 semaphore, mutex dan db
    // Mutex dipakai untuk readers,
    // dan db dipakai untuk writers.
    // jika nilai pada semaphore db <= 0 
    // maka tidak ada yang dapat mengakses buffer
    // selain thread yang bersangkutan.
    // tetapi tidak sama dengan mutex.
    // terlihat di sini bahwa algoritma ini 
    // adalah memberikan prioritas lebih 
    // kepada readers.
    // jika terlalu banyak readers datang bersamaan,
    // writers dapat sarving.
    private int banyakReader;
    Semaphore mutex;
    Semaphore db;
    private static final int NAP_TIME = 15;

    public Database() {
        banyakReader = 0;
        mutex = new Semaphore(1);
        db = new Semaphore(1);
    }

    public static void tunggu() {
        int sleepTime = (int) (NAP_TIME * Math.random());
        try {
            Thread.sleep(sleepTime * 1000);
        } catch (InterruptedException e) {}
    }

    public int mulaiBaca() {

        // Menutup resource agar tidak ada 
        // thread lain mengaksesnya sampai proses
        // masuk selesai.
        mutex.tutup();

        // menambah jumlah reader, agar diketahui
        // jumlah reader yang sedang mengakses resource.
        ++banyakReader;
        if (banyakReader == 1) {

            // jika reader pertama, tutup akses writer ke resource
            db.tutup();
        }

        // membuka mutex, agar reader lain dapat 
        // ikut membaca resource.
        mutex.buka();
        return banyakReader;
    }

    public int selesaiBaca() {

        // Menutup resource agar tidak ada 
        // thread lain mengaksesnya sampai proses
        // keluar masuk selesai
        mutex.tutup();

        // mengurangi jumlah reader
        --banyakReader;
        if (banyakReader == 0) {

            // jika ini adalah thread reader yang 
            // terakhir membaca, buka kembali
            // akses data agar writer dapat masuk.
            db.buka();
        }
        mutex.buka();
        System.out.println("Reader count = " + banyakReader);
        return banyakReader;
    }

    public void mulaiTulis() {

        // menutup akses oleh thread lain
        db.tutup();
    }

    public void selesaiTulis() {

        // membuka akses oleh thread lain.
        db.buka();
    }
}
