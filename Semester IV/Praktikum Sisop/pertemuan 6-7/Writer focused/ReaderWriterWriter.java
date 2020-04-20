//Class utama yang menjalankan keseluruhan program
// di class ini tidak diletakkan satupun method.
public class ReaderWriterWriter {

    private static int NUM_OF_READERS = 3;
    private static int NUM_OF_WRITERS = 2;

    public static void main(final String[] args) {

        // Inisialisasi data, terdapat array Reader dan Writer 
        // dengan jumlah yang telah ditentukan.
        final Database server = new Database();
        final Reader[] readerArray = new Reader[NUM_OF_READERS];
        final Writer[] writerArray = new Writer[NUM_OF_WRITERS];

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

    private final Database server;
    private final int readerNum;

    public Reader(final int r, final Database db) {
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

    private final Database server;
    private final int writerNum;

    public Writer(final int w, final Database db) {
        writerNum = w;
        server = db;
    }

    // Proses dari writer cycle.
    public void run() {

        int writerCount;

        while (true) {
            System.out.println("Writer " + writerNum + " is sleeping.");
            Database.tunggu();
            System.out.println("Writer " + writerNum + " wants to write.");
            writerCount = server.mulaiTulis();
            // System.out.println("Writer " + writerNum + " has entered writing queue.");
            System.out.println("Writer " + writerNum + " is writing.");
            Database.tunggu();
            System.out.println("Writer " + writerNum + " is done writing.");
            writerCount = server.selesaiTulis();
            
        }
    }
}

// Class semaphore untuk mengontrol state thread
final class Semaphore {

    private int value;

    public Semaphore() { value = 0; }

    public Semaphore(final int v) { value = v; }

    public synchronized void tutup() {

        while (value < 1) {

            // jika value semaphore kurang dari 1, 
            // maka thread akan masuk waiting state.
            try {
                wait();
            } catch (final InterruptedException e) {}
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

    // jumlah semaphore yang tadinya hanya 2
    // pada rule readers priority
    // ditambah menjadi 4.
    // rmutex dan wmutex dipakai agar tidak
    // terjadi race condition pada 
    // baik reader maupun writer.
    // db menunjukkan resource
    // readTry untuk mencegah reader menyela
    // saat writer sedang mengakses db.
    private int banyakReader, banyakWriter;
    Semaphore rmutex, db, wmutex, readTry;
    private static final int NAP_TIME = 15;

    public Database() {
        banyakReader = 0;
        banyakWriter = 0;
        rmutex = new Semaphore(1);
        wmutex = new Semaphore(1);
        db = new Semaphore(1);
        readTry = new Semaphore(1);
    }

    public static void tunggu() {
        final int sleepTime = (int) (NAP_TIME * Math.random());
        try {
            Thread.sleep(sleepTime * 1000);
        } catch (final InterruptedException e) {}
    }

    public int mulaiBaca() {

        
        // Menutup resource agar tidak ada 
        // reader lain mengaksesnya sampai proses
        // masuk selesai.
        // readTry.tutup() menyebabkan tidak ada
        // reader yang dapat mencoba masuk
        readTry.tutup();
        rmutex.tutup();

        // menambah jumlah reader, agar diketahui
        // jumlah reader yang sedang mengakses resource.
        ++banyakReader;
        if (banyakReader == 1) {

            // jika reader pertama, tutup akses writer ke resource
            db.tutup();
        }

        // membuka rmutex, agar reader lain dapat 
        // ikut membaca resource.
        rmutex.buka();

        // memberikan akses pada reader lain.
        readTry.buka();
        return banyakReader;
    }

    public int selesaiBaca() {

        // Menutup resource agar tidak ada 
        // thread lain mengaksesnya sampai proses
        // keluar masuk selesai
        rmutex.tutup();

        // mengurangi jumlah reader
        --banyakReader;
        if (banyakReader == 0) {

            // jika ini adalah thread reader yang 
            // terakhir membaca, buka kembali
            // akses data agar writer dapat masuk.
            db.buka();
        }
        rmutex.buka();
        System.out.println("Reader count = " + banyakReader);
        return banyakReader;
    }

    public int mulaiTulis() {

        // menutup akses agar tidak terjadi race condition
        wmutex.tutup();
        ++banyakWriter;

        if (banyakWriter == 1){

            // menutup akses oleh reader yang mencoba masuk.
            readTry.tutup();
        }
            
        // menutup akses oleh thread lain
        db.tutup();
        
        // membuka akses untuk writer yang ingin menulis agar dapat mengantri
        wmutex.buka();
        
        return banyakWriter;
    }
    
    public int selesaiTulis() {
        
        
        // membuka akses oleh thread lain.
        db.buka();
        
        // menutup akses agar tidak ada race condition
        wmutex.tutup();
        --banyakWriter;
        
        if(banyakWriter == 0) {

            // saat writer terakhir selesai
            // ia harus memberikan akses
            // kepada reader yang sudah mengantri.
            readTry.buka();
        }
        
        // membuka akses bagi writer lain.
        wmutex.buka();
        System.out.println("Writer waiting: " + banyakWriter);
        return banyakWriter;
    }
}
