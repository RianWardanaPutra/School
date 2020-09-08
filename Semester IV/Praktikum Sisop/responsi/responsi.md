1. jawaban no 1

```sh
mkdir UGM
cd UGM
mkdir dirA dirB dirC dirD dirE
touch fileA fileB fileC
cp fileA dirD/
mv fileA dirA/
mv fileB dirB/
mv fileC dirC/
mv dirA dirB/
mv -t dirE/ dirC dirD
```

3. jawaban no 3

[kode ke no 3](3.c)

Program tersebut adalah simulasi producer consumer problem. Producer dan consumer mengakses resource (buffer) yang sama dengan ukuran terbatas secara bergantian.

Algoritma ini tidak mendukung penggunaan resource secara bersamaan, maka dari itu digunakan semaphore. Hal ini juga diterapkan sebagai simulasi menghindari deadlock yang diakibatkan penggunaan resource secara bersamaan.

Metode ini bisa digunakan untuk menyelesaikan Reader/Writer problem, karena secara prinsip sama, yaitu penggunaan resource secara bergantian.

4. jawaban no 4

[kode ke no 4](4.cpp)

Algoritma yang digunakan adalah FCFS (First Come First Serve) atau FIFO (First In First Out), yaitu setiap proses yang masuk ke dalam antrian terlebih dahulu, dikerjakan terlebih dahulu.

Head selalu bergerak mencari sektor selanjutnya sesuai urutan. Head mungkin melewati sektor dan silinder yang memiliki pekerjaan, tetapi akan melewatinya begitu saja jika proses tersebut belum tiba waktunya untuk dikerjakan sebelum proses lain selesai.

5. jawaban no 5

[kode ke no 5](5.cpp)

Program ini telah dimodifikasi, sehingga dapat melakukan pengecekan terhadap blok yang telah digunakan dan mengurangi maupun menambah ukuran file, serta blok yang digunakan pun ter-update. Fungsi yang ditambahkan adalah:
```cpp
vector<int> editData(int number, int ch, vector<int> used)
```
Dengan menggunakan vector sebagai container untuk angka blok yang telah digunakan.
