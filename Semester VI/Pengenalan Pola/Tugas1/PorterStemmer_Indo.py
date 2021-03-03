"""
Implementasi Porter Stemmer untuk Bahasa Indonesia diadaptasi dari
https://snowballstem.org/algorithms/indonesian/stemmer.html
dan https://eprints.illc.uva.nl/740/1/MoL-2003-02.text.pdf
Algoritma stemming adalah:
    1. Hapus partikel
    2. Hapus imbuhan kepemilikan
    3. Hapus 1st order _prefix
    if [3] fails:
        4a. Hapus 2nd order _prefix
        5a. Hapus suffix
        6a. End, return stem
    else:
        4b. Hapus suffix
            if [4b] fails:
                5c. End, return stem
        5b. Hapus 2nd order _prefix
        6b. End, return stem
"""
import re

kata_ai = [
    'abai', 'acai', 'adai', 'badai', 'aderai', 'aduhai', 'agai', 'agungrai', 'ajai',
    'alai', 'belai', 'altai', 'amahai', 'amai', 'ambai', 'ampai', 'amunsai', 'amuntai',
    'anai', 'anaksungai', 'ancai', 'andai', 'anggai', 'ao dai', 'aodai', 'arai', 'arombai',
    'asai', 'awai', 'bagai', 'bai', 'balai', 'bangai', 'banggai', 'bangkai', 'bangsai',
    'bantai', 'banzai', 'barai', 'barongsai', 'batai', 'batang anai', 'baterai', 'belalai',
    'belantai', 'belu-belai', 'bengkalai', 'benyai', 'ramai', 'randai', 'rangkai', 'rantai',
    'desai', 'jumbai', 'lalai', 'pandai', 'santai', 'setai', 'tatai', 'rumbai', 'untai',
    'bidai', 'bilai', 'bingkai', 'binjai', 'birai', 'bisai', 'bizurai', 'bombai', 'bonai',
    'bonglai', 'bonsai', 'buai', 'bulai', 'bulalai', 'bungarampai', 'bunglai', 'bunjai',
    'burai', 'busai', 'cabai', 'cadai', 'mencadai', 'cai', 'canai', 'candai', 'canggai',
    'capai', 'capcai', 'cemperai', 'cenduai', 'cengkurai', 'cerai', 'ceratai', 'ceremai',
    'cermai', 'cerpelai', 'cetai', 'chiangmai', 'cindai', 'cipai', 'ciremai', 'cuai',
    'cukai', 'cupai', 'curai', 'cutbrai', 'dacai', 'dai', 'damai', 'dawai', 'dembai',
    'denai', 'departementai', 'derai', 'disigai', 'drai', 'duai', 'dubai', 'duhai', 'dumai',
    'embuai', 'enjelai', 'erai', 'esai', 'essai', 'etai', 'fai', 'gabai', 'gadai', 'gagai',
    'gai', 'galai', 'gapai', 'menggapai', 'garai', 'gawai', 'gelamai', 'gelembai', 'gemelai',
    'gemulai', 'geragai', 'gerai', 'gerapai', 'gontai', 'gulai', 'gulambai', 'gunjai',
    'guntai', 'habotai', 'hai', 'lai', 'halai', 'handai', 'hantai', 'hasai', 'hawai',
    'hayai', 'helai', 'honai', 'hudai', 'hyundai', 'ilai', 'inai', 'indai', 'inkai',
    'intai', 'jamiroquai', 'jebai', 'jelai', 'jerabai', 'jerambai', 'jerumbai', 'jujai',
    'julai', 'jundai', 'juntai', 'jurai', 'kai', 'kajai', 'kalai', 'mengalai', 'kansai',
    'kapai', 'kasai', 'katai', 'kedai', 'kedangkai', 'kedekai', 'kedelai', 'kejai', 'kelai',
    'kelambai', 'sikelambai', 'kelarai', 'keledai', 'kelembuai', 'kelempai', 'kelepai',
    'keluai', 'kempetai', 'kenidai', 'kenpetai', 'kepai', 'kerai', 'kerangkai', 'kerawai',
    'kerepai', 'kernai', 'mengernai', 'kerpai', 'kersai', 'ketai', 'kiai', 'kijai', 'kilai',
    'kirai', 'kisai', 'mengisai', 'kiyai', 'komersiai', 'kotai', 'kpai', 'krai', 'kuai',
    'kucai', 'mengucai', 'kudai', 'kukai', 'kulai', 'kulapai', 'kumai', 'kumpai', 'kunai',
    'kundai', 'kurai', 'kutai', 'kyai', 'lambai', 'lamdukpai', 'lampai', 'landai', 'langgai',
    'langkai', 'langlai', 'langsai', 'lanjai', 'lansai', 'lantai', 'larai', 'lawai', 'lebai',
    'lelai', 'lembahanai', 'lembai', 'lempenai', 'lengai', 'lengkai', 'lenyai', 'lepai', 'lerai',
    'letai', 'letah-letai', 'licurai', 'lihai', 'limbai', 'lipai', 'lolai', 'lontai', 'lulai',
    'luncai', 'lunglai', 'lunyai', 'lutilenyai', 'mahaligai', 'mahligai', 'mai', 'malai', 'malai',
    'maligai', 'mamai', 'mampai', 'manai', 'mandai', 'manggarai', 'mangsai', 'marapulai', 'masai',
    'maskapai', 'materai', 'mawai', 'renyai', 'metai', 'meterai', 'mikrountai', 'misai', 'moai',
    'monolinguai', 'morotai', 'muai', 'muaythai', 'mulai', 'mumbai', 'murai', 'ngarai', 'ngurahrai',
    'nilai', 'njai', 'nyai', 'nyarai', 'nyenyai', 'pacai', 'pai', 'pakai', 'palai', 'panai',
    'pangkai', 'paniai', 'pantai', 'partai', 'pasai', 'pawai', 'pecai', 'perai', 'perai',
    'perisai', 'permai', 'pesai', 'petai', 'petsai', 'piawai', 'pindai', 'pingai', 'pirai',
    'poksai', 'puadai', 'pulai', 'punai', 'punggai', 'purai', 'radai', 'meradai', 'rai',
    'rambai', 'rampai', 'ranai', 'merandai', 'rangai', 'merangai', 'rapai', 'merapai', 'rarai',
    'merarai', 'rasai', 'merasai', 'rawai', 'relai', 'merelai', 'remai', 'rembunai', 'rempenai',
    'remunggai', 'renai', 'renai', 'renyai', 'rigai', 'rinai', 'merinai', 'ringkai', 'rinnai',
    'rinyai', 'ripai', 'rombebai', 'ruai', 'rubai', 'runtai', 'seruntai', 'runyai', 'sadai',
    'sagai', 'sai', 'sakai', 'salai', 'sampai', 'samurai', 'sangai', 'sangrai', 'sanjai',
    'sansai', 'sapai', 'satai', 'sawai', 'sebagai', 'sebai', 'sedawai', 'sehelai', 'selai',
    'selampai', 'selesai', 'semai', 'semampai', 'semarai', 'seminai', 'sempalai', 'senarai',
    'senigai', 'sensai', 'sepai', 'seprai', 'serabai', 'serai', 'serawai', 'serindai',
    'serkai', 'serunai', 'sesampai', 'sesuai', 'setangkai', 'shanghai', 'sidai', 'sigai',
    'sijundai', 'sikai', 'simbai', 'simpai', 'sinai', 'siomai', 'sipai', 'slai', 'olai',
    'sondai', 'sorak-sorai', 'suai', 'sungai', 'sungkai', 'supai', 'suplai', 'surai', 'survai',
    'talai', 'tanai', 'tanggai', 'tangkai', 'tapai', 'tasai', 'telangkai', 'tembikai', 'tempilai',
    'tempunai', 'tenggadai', 'umbai', 'thai', 'tikai', 'tirai', 'mirai', 'tokai', 'tuai',
    'tukai', 'menukai', 'tunai', 'tungganai', 'tungkai', 'tupai', 'udai', 'ungkai', 'urai',
    'usai', 'wahai', 'wai', 'wizurai', 'yahrai', 'zai', 'zumbai']

kata_ai = dict(zip(kata_ai, kata_ai))

kata_dasar_k = [
    'kerja', 'kabar', 'kurang', 'kendara', 'kecil', 'kali', 'kempis', 'kiri', 
    'kandang', 'kembang', 'kutip', 'kukus', 'kuning', 'kirim', 'kasihan', 'kendali',
    'kejar', 'kelompok', 'kuat'
]

kata_dasar_k = dict(zip(kata_dasar_k, kata_dasar_k))


class PorterStyleStemmer:
    def __init__(self):
        """
        Papernya memaparkan penghitungan integer _measure untuk menghitung
        jumlah vokal (aiueo). Dihitung pada kata awal, kemudian dihitung
        kembali sejalan dengan pengurangan imbuhan."""

        self._buffer = ''

        """
        Kode angka untuk jenis _prefix yang dihapus:

        0: tidak ada/tidak termasuk daftar ini
        1: 'di' atau 'meng' atau 'ter'
        2: 'per'
        3: 'ke' atau 'peng'
        4: 'ber'

        di antara bentuk-bentuk di atas, terdapat varian lain seperti
        'meng' termasuk 'men', 'me', 'meny', 'mem'.
        """

        self._prefix = 0

        self._suffix_dihapus = False

        # bentuk kata benda dengan menggunakan ke-an
        self._bentuk_kb_ke = False

    def _hapus_partikel(self):
        # method yang menghapus partikel seru seperti pada 'pakailah' atau 'benarkah'

        kata = self._buffer
        self._buffer = re.sub(r'(lah|kah|pun)$', '', self._buffer)
        if kata != self._buffer:
            self._measure -= 1

    def _hapus_kepemilikan(self):
        kata = self._buffer
        self._buffer = re.sub(r'(ku|mu|nya)$', '', self._buffer)
        if kata != self._buffer:
            self._measure -= 1

    def _cek_suffix_kan(self):
        """Pengecekan suffix kan

        Method ini mengecek apakah suatu kata dengan akhiran kan jika dipotong
        akan menghasilkan kata dasar yang valid atau tidak. Misal
        peledakan tidak menjadi leda tetapi ledak.

        Jika kata memiliki _prefix 'ke', 'peng', 'per', maka kata tidak mungkin
        memiliki suffix 'kan', artinya kan adalah bagian dari kata dasar.
        Penjelasan lebih lengkap terdapat pada link algoritma snowball.

        Returns
        -------
        True jika _prefix tidak dalam {ke, peng, per}
        """

        return self._prefix != 3 and self._prefix != 2

    def _cek_suffix_an(self):
        """Pengecekan suffix an

        Apabila kata memiliki _prefix 'di', 'meng', 'ter', maka kata tidak
        mungkin memiliki suffix 'an', sehingga method ini mengecek apakah
        kata memiliki _prefix 'di', 'meng', 'ter', jika true maka 'an' pada
        kata adalah suffix.

        Returns
        -------
        True kata tidak mengandung {di, meng, ter}
        """

        return self._prefix != 1

    def _cek_suffix_i(self):
        """Pengecekan suffix 'i' (tidak dalam {ke, peng, ber})

        Dalam Bahasa Indonesia, terdapat imbuhan 'i' seperti 'digurui',
        'menggurui', 'mengamini' dan lain sebagainya. Namun untuk menghapus
        imbuhan 'i' perlu diperhatikan kata-kata serapan dari bahasa asing 
        seperti 'televisi', 'komunikasi', 'atensi', dan lainnya. Maka dari
        itu, dalam method ini dilakukan pengecekan apakah kata berakhiran
        '-si' atau tidak untuk mencegah kata serapan tersebut terpotong.
        Namun perlu diperhatikan bahwa method ini tidak bisa mengenali kata
        dasar yang menggunakan akhiran 2 huruf vokal *i misal '-ai' seperti
        pada 'pantai', 'santai', 'bangkai'. Hal ini yang merupakan salah satu
        kelemahan algoritma ini, menyebabkan kata-kata tersebut akan terpotong.
        Akan tetapi kata yang berakhiran 2 huruf vokal tersebut lebih sedikit
        daripada kata yang dapat diimbuhi 'i', sehingga untuk menambah 
        keefektifan dapat ditambah pengecekan wordlist.

        Returns
        -------
        True jika kata tidak berakhiran 'si' dan _prefix != {ke, peng, ber}
        """

        return self._prefix <= 2 and \
            not self._buffer.endswith('si')

    def _hapus_suffix(self):
        """Hapus suffix 'kan' 'an' 'i'

        Proses penghapusan imbuhan -kan, -an, -i.
        penghapusan hanya dilakukan sekali pada tiap kata yang diproses
        """

        if self._buffer.endswith('kan') and \
                self._cek_suffix_kan():
            self._buffer = self._buffer[:-3]
            self._measure -= 1
            self._suffix_dihapus = True
            return

        if self._buffer.endswith('an') and \
                self._cek_suffix_an():
            self._buffer = self._buffer[:-2]
            self._measure -= 1
            self._suffix_dihapus = True
            return

        if self._buffer.endswith('i') and \
                self._cek_suffix_i() and \
                self._buffer not in kata_ai:
            self._buffer = self._buffer[:-1]
            self._measure -= 1
            self._suffix_dihapus = True
        elif self._buffer.endswith('i') and self._buffer in kata_ai:
            self._suffix_dihapus = True
            pass

    def _hapus_suffix_meng(self, kata):
        """Hapus suffix 'kan' 'an' 'i'

        Method ini berbeda dengan method di atas karena method ini mengambil parameter 
        dan tidak ditujukan untuk mengubah self._buffer
        """

        original = kata
        if kata.endswith('kan') and \
                self._cek_suffix_kan():
            kata = kata[:-3]
            self._measure -= 1
            # self._suffix_dihapus = True
            return kata

        if kata.endswith('an') and \
                self._cek_suffix_an():
            kata = kata[:-2]
            self._measure -= 1
            # self._suffix_dihapus = True
            return kata

        if kata.endswith('i') and \
                self._cek_suffix_i() and \
                kata not in kata_ai:
            kata = kata[:-1]
            self._measure -= 1
            # self._suffix_dihapus = True
            return kata
        elif kata.endswith('i') and kata in kata_ai:
            # self._suffix_dihapus = True
            pass

        return original

    def _prefix_1(self):
        self._prefix = 1
        self._measure -= 1
        return ''

    def _prefix_2(self):
        self._prefix = 2
        self._measure -= 1
        return ''

    def _prefix_3(self):
        self._prefix = 3
        self._measure -= 1
        return ''

    def _hapus_prefix_first_order(self):

        # di meng me men ter
        if re.match(r'^(di|ter)', self._buffer):
            self._buffer = re.sub(r'^(di|ter)',
                                  self._prefix_1(), self._buffer)
            return True
        if re.match(r'^meng[aiueo]', self._buffer):
            temporary = re.sub(r'^meng([aiueo])', r'k\1', self._buffer)
            temporary = self._hapus_suffix_meng(temporary)
            if temporary in kata_dasar_k:
                self._buffer = temporary
            else:
                self._buffer = temporary[1:]
            self._prefix = 1
            return True

        if re.match(r'^meng[^aiueo]', self._buffer):
            self._buffer = re.sub(r'^meng', self._prefix_1(), self._buffer)
            return True

        if re.match(r'^men[aiueo]', self._buffer):
            self._buffer = re.sub(
                r'^men([aiueo])', r't\1' + self._prefix_1(), self._buffer)
            return True

        if re.match(r'^men[^aiueoyg]', self._buffer):
            self._buffer = re.sub(r'^men', self._prefix_1(), self._buffer)
            return True

        if re.match(r'^me[^aiueomn]', self._buffer):
            self._buffer = re.sub(r'^me', self._prefix_1(), self._buffer)
            return True

        # ke peng pen (konsonan)
        if re.match(r'^ke', self._buffer):
            self._buffer = re.sub(r'^ke', self._prefix_3(), self._buffer)
            self._bentuk_kb_ke = True
            return True

        if re.match(r'^(peng|pen)[^aiueoy]', self._buffer):
            self._buffer = re.sub(
                r'^(peng|pen)([^aiueo]{1})', r'\2' + self._prefix_3(), self._buffer)
            return True

        # quick fix untuk kata-kata yang sesuai pola (pen(t)erima, peng(k)eriting)
        if re.match(r'(peng|pen)[aiueo]', self._buffer):
            if self._buffer.startswith('peng'):
                self._buffer = re.sub(
                    r'^peng([aiueo])', r'k\1' + self._prefix_3(), self._buffer)
            else:
                self._buffer = re.sub(
                    r'^pen([aiueo])', r't\1' + self._prefix_3(), self._buffer)
            return True

        # meny dan peny
        if re.match(r'^(meny|peny)[aiueo]', self._buffer):
            if self._buffer.startswith('meny'):
                self._buffer = re.sub(
                    r'^meny([aiueo])', r's\1' + self._prefix_1(), self._buffer)
            else:
                self._buffer = re.sub(
                    r'^peny([aiueo])', r's\1' + self._prefix_3(), self._buffer)
            return True

        # mem dan pem (konsonan)
        if re.match(r'^(mem|pem)[^aiueo]', self._buffer):
            if self._buffer.startswith('mem'):
                self._buffer = re.sub(
                    r'^mem([^aiueo])', r'\1' + self._prefix_1(), self._buffer)
            else:
                self._buffer = re.sub(
                    r'^pem([^aiueo])', r'\1' + self._prefix_3(), self._buffer)
            return True

        # mem dan pem (vokal)
        if re.match(r'^(mem|pem)[aiueo]', self._buffer):
            if self._buffer.startswith('mem'):
                self._buffer = re.sub(
                    r'^mem([aiueo])', r'p\1' + self._prefix_1(), self._buffer)
            else:
                self._buffer = re.sub(
                    r'^pem([aiueo])', r'p\1' + self._prefix_3(), self._buffer)
            return True

        return False

    def _hapus_prefix_second_order(self):
        if re.match(r'^pelajar', self._buffer):
            self._buffer = 'ajar'
            self._prefix = 2
            self._measure = 2
            return True

        if self._buffer == 'belajar':
            self._buffer = 'ajar'
            self._prefix = 4
            self._measure = 2
            return True

        if re.match(r'^(per|pe)[^aiueon]', self._buffer):
            self._buffer = re.sub(r'^(per|pe)', '', self._buffer)
            self._prefix = 2
            self._measure -= 1
            return True

        if self._buffer.startswith('ber'):
            self._buffer = re.sub(r'^ber', '', self._buffer)
            self._prefix = 4
            self._measure -= 1
            return True

        if re.match(r'^be[^aiueo]{1}(er)', self._buffer):
            self._buffer = re.sub(r'^be([^aiueo](er))', r'\1', self._buffer)
            self._prefix = 4
            self._measure -= 1
            return True

        return False

    def stem(self, kata):
        self._buffer = kata

        # entah mengapa _prefix harus diinisiasikan ulang
        self._prefix = 0
        self._measure = len(re.findall(r'[^aiueo]*[aiueo]', self._buffer))
        if self._measure > 2:
            self._hapus_partikel()
            if self._measure > 2:
                self._hapus_kepemilikan()

        kata_asal = self._buffer
        if self._measure > 2:
            berubah = self._hapus_prefix_first_order()
            if self._bentuk_kb_ke:
                berubah = self._hapus_prefix_first_order()
                self._prefix = 3
            if self._measure > 2:
                self._hapus_suffix()
                if not berubah and self._measure > 2:
                    self._hapus_prefix_second_order()
        if self._buffer == kata_asal:
            self._hapus_prefix_second_order()
            if self._measure > 2:
                if not self._suffix_dihapus:
                    self._hapus_suffix()
        return self._buffer


# contoh pemakaian
stemmer = PorterStyleStemmer()
print(stemmer.stem('kepemilikan'))

print(stemmer.stem('kebahagiaan'))

print(stemmer.stem('ketersediaan'))

