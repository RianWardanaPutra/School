from PorterStemmer_Indo import PorterStyleStemmer
import re
punctuations = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~\n"

def folder():
    for i in range(10):
        continue
    # tokenization of text
    # def tokenization(docs: str):
    #     """tokenization is a function to get tokens of a string

    #     Tokens are words, that have lexical meaning and can be used for determining
    #     what kind of document or text the text is about. Tokens have any
    #     regular punctuations stripped. Posessive suffix (-'s) is also removed

    #     Params
    #     -------
    #     docs: string
    #         string to be parsed into tokens

    #     Returns
    #     --------
    #     tokens: array of string
    #         a list of result tokens from docs
    #     """

    #     tokens = []
    #     raw = docs.split()
    #     for word in raw:
    #         clean_word = word.lower()
    #         for character in punctuations:
    #             cleaned = clean_word.strip(character)
    #             if len(cleaned) < len(clean_word):
    #                 clean_word = cleaned

    #         for character in punctuations[::-1]:
    #             cleaned = clean_word.strip(character)
    #             if len(cleaned) < len(clean_word):
    #                 clean_word = cleaned

    #         if clean_word[-2:] == "'s":
    #             clean_word = word.strip("'s")

    #         if clean_word not in tokens:
    #             contains_punctuations = False
    #             for i in [x in clean_word for x in punctuations]:
    #                 if i:
    #                     contains_punctuations = True

    #             if clean_word.isalnum() or contains_punctuations:
    #                 buff = ''
    #                 for i in clean_word:
    #                     if i.isalpha():
    #                         buff += i
    #                     if not i.isalpha():
    #                         break
    #                 clean_word = buff

    #             if clean_word != '' and not re.match(r'^http(.*)', clean_word):
    #                 tokens.append(clean_word.lower())
    #     return tokens
    pass

def get_title(raw_html):
    regx = re.compile('<title.*>(.*?)</title>')
    match = re.search(regx, raw_html, re.DOTALL, re.I)
    title = match.group(1) if match else 'No title'
    return title

def strip_script(raw_html):
    regx = re.compile('(?is)(^.*)<script[^>]*>(.*)</script>(.*$)')
    regx2 = re.compile('(?is)(^.*)<style[^>]*>(.*)</style>(.*$)')
    content = re.sub(regx, r'\1 \3', raw_html)
    content = re.sub(regx2, r'\1 \3', raw_html)
    return content

def strip_html(raw_html):
    """Strip html tags

    fungsi ini menghapus tag html dari teks biasa menggunakan regex
    """

    clean_regx = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    clean_text = re.sub(clean_regx, '', raw_html)
    return clean_text

class Stopwords_Remover:
    """Stopwords Remover

    Class ini berfungsi untuk membuat objek untuk menghapus stopwords
    dan mengembalikan teks yang telah dihapus stopwords-nya.
    Params
    ------
    None

    Returns
    -------
    Object -> untuk menghapus stopwords

    Methods
    -------
    get_stopwords: list stopwords yang akan difilter
        Usage: Object.get_stopwords()

    remove: method untuk menghapus stopwords
        Usage: Object.remove(text)
    """

    def __init__(self):
        words = self.get_stopwords()
        self.stopwords = self._stopwords_dictionary(words)

    def _stopwords_dictionary(self, words):
        return dict(zip(words, words))

    def remove(self, text):
        """remove: method untuk menghapus stopwords
        Usage: Object.remove(text)
        Params
        ------
        text: String -> teks yang akan dihapus stopwords-nya

        Returns
        -------
        filtered_words: String -> hasil teks yang telah dihilangkan stopwords-nya
        """

        raw_text = text.split()
        filtered_words = [
            word for word in raw_text if word not in self.stopwords]
        return ' '.join(filtered_words)

    def get_stopwords(self):
        """get_stopwords: list stopwords yang akan difilter
        Usage: Object.get_stopwords()
        Params
        ------
        None

        Returns
        -------
        list stopwords yang dipakai (List[str])
        """

        return [
            'a', 'ada', 'adalah', 'adanya', 'adapun', 'agak', 'agaknya', 'agar', 'akan', 'akankah', 'akhir',
            'akhiri', 'akhirnya', 'aku', 'akulah', 'amat', 'amatlah', 'anda', 'andalah', 'antar', 'antara',
            'antaranya', 'apa', 'apaan', 'apabila', 'apakah', 'apalagi', 'apatah', 'arti', 'artinya', 'asal',
            'asalkan', 'atas', 'atau', 'ataukah', 'ataupun', 'awal', 'awalnya', 'b', 'bagai', 'bagaikan',
            'bagaimana', 'bagaimanakah', 'bagaimanapun', 'bagainamakah', 'bagi', 'bagian', 'bahkan', 'bahwa',
            'bahwasannya', 'bahwasanya', 'baik', 'baiklah', 'bakal', 'bakalan', 'balik', 'banyak', 'bapak',
            'baru', 'bawah', 'beberapa', 'begini', 'beginian', 'beginikah', 'beginilah', 'begitu', 'begitukah',
            'begitulah', 'begitupun', 'bekerja', 'belakang', 'belakangan', 'belum', 'belumlah', 'benar',
            'benarkah', 'benarlah', 'berada', 'berakhir', 'berakhirlah', 'berakhirnya', 'berapa', 'berapakah',
            'berapalah', 'berapapun', 'berarti', 'berawal', 'berbagai', 'berdatangan', 'beri', 'berikan',
            'berikut', 'berikutnya', 'berjumlah', 'berkali-kali', 'berkata', 'berkehendak', 'berkeinginan',
            'berkenaan', 'berlainan', 'berlalu', 'berlangsung', 'berlebihan', 'bermacam', 'bermacam-macam',
            'bermaksud', 'bermula', 'bersama', 'bersama-sama', 'bersiap', 'bersiap-siap', 'bertanya',
            'bertanya-tanya', 'berturut', 'berturut-turut', 'bertutur', 'berujar', 'berupa', 'besar',
            'betul', 'betulkah', 'biasa', 'biasanya', 'bila', 'bilakah', 'bisa', 'bisakah', 'boleh', 'bolehkah',
            'bolehlah', 'buat', 'bukan', 'bukankah', 'bukanlah', 'bukannya', 'bulan', 'bung', 'c', 'cara',
            'caranya', 'cukup', 'cukupkah', 'cukuplah', 'cuma', 'd', 'dahulu', 'dalam', 'dan', 'dapat', 'dari',
            'daripada', 'datang', 'dekat', 'demi', 'demikian', 'demikianlah', 'dengan', 'depan', 'di', 'dia',
            'diakhiri', 'diakhirinya', 'dialah', 'diantara', 'diantaranya', 'diberi', 'diberikan', 'diberikannya',
            'dibuat', 'dibuatnya', 'didapat', 'didatangkan', 'digunakan', 'diibaratkan', 'diibaratkannya',
            'diingat', 'diingatkan', 'diinginkan', 'dijawab', 'dijelaskan', 'dijelaskannya', 'dikarenakan',
            'dikatakan', 'dikatakannya', 'dikerjakan', 'diketahui', 'diketahuinya', 'dikira', 'dilakukan',
            'dilalui', 'dilihat', 'dimaksud', 'dimaksudkan', 'dimaksudkannya', 'dimaksudnya', 'diminta',
            'dimintai', 'dimisalkan', 'dimulai', 'dimulailah', 'dimulainya', 'dimungkinkan', 'dini', 'dipastikan',
            'diperbuat', 'diperbuatnya', 'dipergunakan', 'diperkirakan', 'diperlihatkan', 'diperlukan',
            'diperlukannya', 'dipersoalkan', 'dipertanyakan', 'dipunyai', 'diri', 'dirinya', 'disampaikan',
            'disebut', 'disebutkan', 'disebutkannya', 'disini', 'disinilah', 'ditambahkan', 'ditandaskan',
            'ditanya', 'ditanyai', 'ditanyakan', 'ditegaskan', 'ditujukan', 'ditunjuk', 'ditunjuki', 'ditunjukkan',
            'ditunjukkannya', 'ditunjuknya', 'dituturkan', 'dituturkannya', 'diucapkan', 'diucapkannya',
            'diungkapkan', 'dong', 'dua', 'dulu', 'e', 'empat', 'enak', 'enggak', 'enggaknya', 'entah', 'entahlah',
            'f', 'g', 'guna', 'gunakan', 'h', 'hadap', 'hai', 'hal', 'halo', 'hallo', 'hampir', 'hanya', 'hanyalah',
            'hari', 'harus', 'haruslah', 'harusnya', 'helo', 'hello', 'hendak', 'hendaklah', 'hendaknya', 'hingga',
            'i', 'ia', 'ialah', 'ibarat', 'ibaratkan', 'ibaratnya', 'ibu', 'ikut', 'ingat', 'ingat-ingat', 'ingin',
            'inginkah', 'inginkan', 'ini', 'inikah', 'inilah', 'itu', 'itukah', 'itulah', 'j', 'jadi', 'jadilah',
            'jadinya', 'jangan', 'jangankan', 'janganlah', 'jauh', 'jawab', 'jawaban', 'jawabnya', 'jelas',
            'jelaskan', 'jelaslah', 'jelasnya', 'jika', 'jikalau', 'juga', 'jumlah', 'jumlahnya', 'justru',
            'k', 'kadar', 'kala', 'kalau', 'kalaulah', 'kalaupun', 'kali', 'kalian', 'kami', 'kamilah', 'kamu',
            'kamulah', 'kan', 'kapan', 'kapankah', 'kapanpun', 'karena', 'karenanya', 'kasus', 'kata', 'katakan',
            'katakanlah', 'katanya', 'ke', 'keadaan', 'kebetulan', 'kecil', 'kedua', 'keduanya', 'keinginan',
            'kelamaan', 'kelihatan', 'kelihatannya', 'kelima', 'keluar', 'kembali', 'kemudian', 'kemungkinan',
            'kemungkinannya', 'kena', 'kenapa', 'kepada', 'kepadanya', 'kerja', 'kesampaian', 'keseluruhan',
            'keseluruhannya', 'keterlaluan', 'ketika', 'khusus', 'khususnya', 'kini', 'kinilah', 'kira',
            'kira-kira', 'kiranya', 'kita', 'kitalah', 'kok', 'kurang', 'l', 'lagi', 'lagian', 'lah', 'lain',
            'lainnya', 'laku', 'lalu', 'lama', 'lamanya', 'langsung', 'lanjut', 'lanjutnya', 'lebih', 'lewat',
            'lihat', 'lima', 'luar', 'm', 'macam', 'maka', 'makanya', 'makin', 'maksud', 'malah', 'malahan',
            'mampu', 'mampukah', 'mana', 'manakala', 'manalagi', 'masa', 'masalah', 'masalahnya', 'masih',
            'masihkah', 'masing', 'masing-masing', 'masuk', 'mata', 'mau', 'maupun', 'melainkan', 'melakukan',
            'melalui', 'melihat', 'melihatnya', 'memang', 'memastikan', 'memberi', 'memberikan', 'membuat',
            'memerlukan', 'memihak', 'meminta', 'memintakan', 'memisalkan', 'memperbuat', 'mempergunakan',
            'memperkirakan', 'memperlihatkan', 'mempersiapkan', 'mempersoalkan', 'mempertanyakan', 'mempunyai',
            'memulai', 'memungkinkan', 'menaiki', 'menambahkan', 'menandaskan', 'menanti', 'menanti-nanti',
            'menantikan', 'menanya', 'menanyai', 'menanyakan', 'mendapat', 'mendapatkan', 'mendatang', 'mendatangi',
            'mendatangkan', 'menegaskan', 'mengakhiri', 'mengapa', 'mengatakan', 'mengatakannya', 'mengenai',
            'mengerjakan', 'mengetahui', 'menggunakan', 'menghendaki', 'mengibaratkan', 'mengibaratkannya',
            'mengingat', 'mengingatkan', 'menginginkan', 'mengira', 'mengucapkan', 'mengucapkannya', 'mengungkapkan',
            'menjadi', 'menjawab', 'menjelaskan', 'menuju', 'menunjuk', 'menunjuki', 'menunjukkan', 'menunjuknya',
            'menurut', 'menuturkan', 'menyampaikan', 'menyangkut', 'menyatakan', 'menyebutkan', 'menyeluruh',
            'menyiapkan', 'merasa', 'mereka', 'merekalah', 'merupakan', 'meski', 'meskipun', 'meyakini', 'meyakinkan',
            'minta', 'mirip', 'misal', 'misalkan', 'misalnya', 'mohon', 'mula', 'mulai', 'mulailah', 'mulanya', 'mungkin',
            'mungkinkah', 'n', 'nah', 'naik', 'namun', 'nanti', 'nantinya', 'nya', 'nyaris', 'nyata', 'nyatanya',
            'o', 'oleh', 'olehnya', 'orang', 'p', 'pada', 'padahal', 'padanya', 'pak', 'paling', 'panjang', 'pantas',
            'para', 'pasti', 'pastilah', 'penting', 'pentingnya', 'per', 'percuma', 'perlu', 'perlukah', 'perlunya',
            'pernah', 'persoalan', 'pertama', 'pertama-tama', 'pertanyaan', 'pertanyakan', 'pihak', 'pihaknya',
            'pukul', 'pula', 'pun', 'punya', 'q', 'r', 'rasa', 'rasanya', 'rupa', 'rupanya', 's', 'saat', 'saatnya', 'saja',
            'sajalah', 'salam', 'saling', 'sama', 'sama-sama', 'sambil', 'sampai', 'sampai-sampai', 'sampaikan', 'sana',
            'sangat', 'sangatlah', 'sangkut', 'satu', 'saya', 'sayalah', 'se', 'sebab', 'sebabnya', 'sebagai',
            'sebagaimana', 'sebagainya', 'sebagian', 'sebaik', 'sebaik-baiknya', 'sebaiknya', 'sebaliknya',
            'sebanyak', 'sebegini', 'sebegitu', 'sebelum', 'sebelumnya', 'sebenarnya', 'seberapa', 'sebesar',
            'sebetulnya', 'sebisanya', 'sebuah', 'sebut', 'sebutlah', 'sebutnya', 'secara', 'secukupnya', 'sedang',
            'sedangkan', 'sedemikian', 'sedikit', 'sedikitnya', 'seenaknya', 'segala', 'segalanya', 'segera',
            'seharusnya', 'sehingga', 'seingat', 'sejak', 'sejauh', 'sejenak', 'sejumlah', 'sekadar', 'sekadarnya',
            'sekali', 'sekali-kali', 'sekalian', 'sekaligus', 'sekalipun', 'sekarang', 'sekaranglah', 'sekecil',
            'seketika', 'sekiranya', 'sekitar', 'sekitarnya', 'sekurang-kurangnya', 'sekurangnya', 'sela', 'selain',
            'selaku', 'selalu', 'selama', 'selama-lamanya', 'selamanya', 'selanjutnya', 'seluruh', 'seluruhnya',
            'semacam', 'semakin', 'semampu', 'semampunya', 'semasa', 'semasih', 'semata', 'semata-mata', 'semaunya',
            'sementara', 'semisal', 'semisalnya', 'sempat', 'semua', 'semuanya', 'semula', 'sendiri', 'sendirian',
            'sendirinya', 'seolah', 'seolah-olah', 'seorang', 'sepanjang', 'sepantasnya', 'sepantasnyalah',
            'seperlunya', 'seperti', 'sepertinya', 'sepihak', 'sering', 'seringnya', 'serta', 'serupa', 'sesaat',
            'sesama', 'sesampai', 'sesegera', 'sesekali', 'seseorang', 'sesuatu', 'sesuatunya', 'sesudah',
            'sesudahnya', 'setelah', 'setempat', 'setengah', 'seterusnya', 'setiap', 'setiba', 'setibanya',
            'setidak-tidaknya', 'setidaknya', 'setinggi', 'seusai', 'sewaktu', 'siap', 'siapa', 'siapakah',
            'siapapun', 'sini', 'sinilah', 'soal', 'soalnya', 'suatu', 'sudah', 'sudahkah', 'sudahlah', 'supaya',
            't', 'tadi', 'tadinya', 'tahu', 'tak', 'tambah', 'tambahnya', 'tampak', 'tampaknya', 'tandas', 'tandasnya',
            'tanpa', 'tanya', 'tanyakan', 'tanyanya', 'tapi', 'tegas', 'tegasnya', 'telah', 'tempat', 'tentang', 'tentu',
            'tentulah', 'tentunya', 'tepat', 'terakhir', 'terasa', 'terbanyak', 'terdahulu', 'terdapat', 'terdiri',
            'terhadap', 'terhadapnya', 'teringat', 'teringat-ingat', 'terjadi', 'terjadilah', 'terjadinya', 'terkira',
            'terlalu', 'terlebih', 'terlihat', 'termasuk', 'ternyata', 'tersampaikan', 'tersebut', 'tersebutlah',
            'tertentu', 'tertuju', 'terus', 'terutama', 'tetap', 'tetapi', 'tiap', 'tiba', 'tiba-tiba', 'tidak',
            'tidakkah', 'tidaklah', 'tiga', 'toh', 'tuju', 'tunjuk', 'turut', 'tutur', 'tuturnya', 'u', 'ucap', 'ucapnya',
            'ujar', 'ujarnya', 'umumnya', 'ungkap', 'ungkapnya', 'untuk', 'usah', 'usai', 'v', 'w', 'waduh', 'wah', 'wahai',
            'waktunya', 'walau', 'walaupun', 'wong', 'x', 'y', 'ya', 'yaitu', 'yakin', 'yakni', 'yang', 'z'
        ]

def remove_punctuations(text):
  for symbol in punctuations:
    text = text.replace(symbol, ' ')
  text = ' '.join([x for x in text.split()])
  return text

def parse_text(text: str):
    result = []
    docs = ''
    for letters in range(len(text)):
        # if letters not in punctuations:
        docs += text[letters]
        if text[letters] == '\n' or letters == len(text) - 1:
            if docs.strip() != '':
                result.append(docs.strip())
            docs = ''
    if docs != '':
        result.append(docs)
    return result

def remove_numbers(bow: list) -> list:
    new_list = []
    for word in bow:
        if word.isalpha():
            new_list.append(word)
    return new_list

def text_preprocessing(raw_html: str) -> list:
    """Teks preprosesing
    
    returns
    -------
    documents: 2d list, [title, list terms]
    """

    raw_html = raw_html.lower()
    title = get_title(raw_html)
    docs = strip_script(raw_html)
    docs = strip_html(docs)
    stopwords = Stopwords_Remover()
    docs = stopwords.remove(docs)
    docs = remove_punctuations(docs)
    bag_of_words = docs.split()
    stemmer = PorterStyleStemmer()
    stemmed_words = []
    for word in bag_of_words:
        res = stemmer.stem(word)
        stemmed_words.append(res)
    stemmed_words = remove_numbers(stemmed_words)
    document = [title, stemmed_words]
    return document


text = """remove: method untuk menghapus stopwords
        Usage: Object.remove(text)
        Params
        ------
        text: String -> teks yang akan dihapus stopwords-nya

        Returns
        -------
        filtered_words: String -> hasil teks yang telah dihilangkan stopwords-nya
        """

data = remove_punctuations(text)
print(data)

text = """Note that type hints are intended for static analysis and for use by linters. 
        Type hints are not used for run-time type checking. Nor are they used for optimization. 2 of 3these
        Also note that type hints are in their infancy. Almost no code in Python has type hints and 
        no analysis tools have been developed to deal with them (as far as I know)."""

text2 = '''KOMPAS.com - Pada akhir tahun 2020, pakar Organisasi Kesehatan Dunia ( WHO) mengatakan bahwa, pandemi Covid-19 ini bisa menjadi endemik. WHO menyatakan, meski pandemi virus corona yang kita hadapi saat ini sangat parah, fenomena ini belum tentu yang besar. Oleh sebab itu, WHO mengingatkan agar dunia bisa belajar untuk hidup berdampingan dengan Covid-19. 
    "Virus (corona) ditakdirkan akan menjadi endemik. Bahkan saat vaksin mulai diluncurkan," kata Profesor David Heymann, ketua kelompok penasihat strategi dan teknis WHO untuk bahaya infeksi. 
    Baca juga: WHO Bisa Saja Cabut Status Pandemi Lebih Cepat di Negara Ini, Asalkan Dia melanjutkan, saat ini dunia sangat berharap adanya herd immunity.
    Entah bagaimana banyak yang percaya, jika banyak orang yang kebal terhadap virus maka angka penularan akan menurun. Heymann yang juga seoranga ahli epidemiologi di London School of Hygiene and Tropical Medicine mengatakan, konsep herd immunity disalahpahami. 
    "Tampaknya takdir (virus corona) SARS-CoV-2 penyebab Covid-19 akan menjadi endemik, seperti halnya 4 virus corona lain yang menginfeksi manusia. Virus akan terus bermutasi saat berkembang biak di sel manusia," imbuhnya seperti dilansir Guardian, 29 Desember 2020. “Kita hidup dalam masyarakat global yang semakin kompleks. Ancaman ini akan terus berlanjut. 
    Jika ada satu hal yang perlu kita pelajari dari pandemi ini, dengan semua tragedi dan kehilangan,kita perlu bertindak bersama. Kita perlu melakukan tindakan yang lebih baik setiap hari.” Kepala ilmuwan WHO, Dr Soumya Swaminathan menambahkan, pelaksanaan vaksinasi Covid-19 tidak berarti menghentikan protokol kesehatan seperti jaga jarak, mencuci tangan, memakai masker, dan menghindari kerumunan di masa depan. 
    Swaminathan berkata, peran pertama dari vaksin adalah untuk mencegah penyakit simptomatik, penyakit parah, dan kematian. Apakah vaksin juga akan mengurangi jumlah infeksi atau mencegah orang menularkan virus, pertanyaan ini masih harus dikaji. 
    Baca juga: Hanya 5 Provinsi yang Bisa Selesai Vaksinasi Covid-19 dalam Setahun "Saya tidak percaya kami memiliki bukti bahwa vaksin apapun dapat mencegah seseorang benar-benar terinfeksi dan karena itu masih dapat menularkannya,” kata Swaminathan. 
    "Jadi, kita perlu berasumsi bahwa orang yang telah divaksinasi juga perlu melakukan tindakan pencegahan yang sama." Di kesempatan yang sama, Direktur jenderal WHO, Tedros Adhanom Ghebreyesus mengatakan bahwa tahun ini kita akan melihat tantangan baru dari Covid-19. Misalnya, varian baru Covid-19 dan tantangan membantu orang yang lelah dengan pandemi.

    Artikel ini telah tayang di Kompas.com dengan judul "WHO Peringatkan, Pandemi Covid-19 Kemungkinan Besar Bakal Jadi Endemik", Klik untuk baca: https://www.kompas.com/sains/read/2021/02/28/170200423/who-peringatkan-pandemi-covid-19-kemungkinan-besar-bakal-jadi-endemik?page=all#page2.
    Penulis : Gloria Setyvani Putri
    Editor : Gloria Setyvani Putri

    Download aplikasi Kompas.com untuk akses berita lebih mudah dan cepat:
    Android: https://bit.ly/3g85pkA
    iOS: https://apple.co/3hXWJ0L'''

documents = parse_text(text)
for i in documents:
    print(f'doc[{documents.index(i)}]: {i}')

stopwords_remover = Stopwords_Remover()

text2 = stopwords_remover.remove(text2)

documents2 = parse_text(text2)
for i in documents2:
    print(f'doc[{documents2.index(i)}]: {i}')

for i in documents2:
    print(tokenization(i))
# print(tokenization(text))

def term_frequency(BoW: list) -> dict:
    """menghitung term frequency

    params
    ------
    BoW: list bag of words sebuah document

    returns
    -------
    tf_dict: dictionary berisi term dan tf indexnya dalam document
    """
    tf_dict = {}
    for term in BoW:
        if term in tf_dict:
            tf_dict[term] += 1
        else:
            tf_dict[term] = 1
    
    words_count = len(BoW)
    for term in tf_dict:
        tf_dict[term] = tf_dict[term] / words_count
    return tf_dict



def compute_idf(corpus: list) -> dict:
    """IDF = N / df(w)
    dengan:
    N = jumlah documents
    df(w) = jumlah documents mengandung kata (w) dalam corpus

    params
    ------
    corpus: list documents (bag of words) yang dijadikan satu

    returns
    -------
    idf_dict: dictionary berisi bobot idf sebuah kata dalam corpus
    """

    import math
    N = len(corpus)
    unique_words = []
    for doc in corpus:
        for word in doc:
            if word not in unique_words:
                unique_words.append(word)
    idf_dict = dict.fromkeys(unique_words, 0)

    pass

