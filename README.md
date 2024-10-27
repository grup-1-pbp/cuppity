# Tugas1 

**Nama Anggota Kelompok :**
1. Abby Shelley Tampubolon
2. Athallah Nadhif Yuzak
3. Ammara Fasha Zia
4. Naya Kusumahayati Rachmi
5. Peter Putra Lesmana
6. Vico Winner Sebastian Aritonang 

Dengan berkembangnya zaman serta pesatnya inovasi di industri teknologi, banyak hal yang dapat dimanfaatkan untuk meningkatkan kesejahteraan, baik untuk diri sendiri maupun masyarakat sekitar. Namun, di Indonesia, masih banyak masyarakat yang belum dapat memaksimalkan penggunaan teknologi. Mereka masih bingung bagaimana teknologi dapat membantu kehidupan mereka.

Yogyakarta, sebuah kota dengan status daerah istimewa, memiliki banyak makanan khas dan restoran yang dapat menjadi sumber penghidupan bagi masyarakat setempat. Selain itu, kota ini menarik para pendatang yang ingin mencoba berbagai makanan khas daerah tersebut. Sayangnya, kurangnya pemanfaatan teknologi menghambat masyarakat setempat dan pendatang dalam mengakses informasi tentang ragam kuliner lokal.

Oleh karena itu, “MANGAN YUK!” hadir untuk membantu masyarakat memamerkan kelezatan masakan mereka dan mempromosikan makanan lokal kepada seluruh pengunjung Yogyakarta. “MANGAN YUK!” adalah sebuah website yang akan mempublikasikan makanan-makanan di daerah Yogyakarta dengan tujuan membantu masyarakat dalam melakukan perdagangan serta membantu masyarakat memanfaatkan teknologi hingga melakukan promosi secara luas. “MANGAN YUK!” didesain dengan memiliki sistem yang interaktif agar user merasa nyaman ketika menjelajahi website kami. Di lain sisi, kami juga menghadirkan sistem admin yang mudah dimengerti agar dapat dipakai oleh masyarakat dengan berbagai macam usia. Pada halaman utama MANGAN YUK! User dapat melihat berbagai macam makanan yang terdapat di Yogyakarta, User juga dapat menggunakan fitur search pada website kami dimana dapat membantu user dalam melakukan pencarian makanan yang sedang user inginkan dan juga memberikan nama restoran yang menyediakan makanan tersebut . Selain itu, pada MANGAN YUK! juga terdapat fitur search by price dimana user dapat mencari makanan dengan harga di bawah atau di atas angka yang user input.



1. Daftar Makanan
   
- Guest (Tidak Login): Bisa melihat daftar makanan berdasarkan kategori
(Chinese, Western, Indonesia, dll.) dan melihat restoran yang menyajikan
makanan tersebut. Tidak bisa menambahkan atau mengedit makanan.
- Admin/Kurator: Bertanggung jawab menambahkan dan mengelola makanan di
website. Mereka memilih makanan yang ditampilkan, mengelompokkannya berdasarkan kategori, dan memastikan informasi yang ditampilkan akurat dan relevan.
- User (Login): Bisa melihat daftar makanan, memberikan ulasan, dan menyimpan makanan favorit.
- Fields : homepage/mainpage (filter dan search)
  - Daftar makanan berdasarkan Kategori (Chinese, Western, Indonesia, dll.)
  - Daftar makanan yang ditampilkan secara umum (berdasarkan kategori,
  nama makanan, harga atau restoran).
  - Filter pencarian harga
  
  Pada bagian ini yang mengerjakan : Peter Putra Lesmana

 2. Pencarian Makanan
    
- Guest (Tidak Login): Bisa mencari makanan berdasarkan kategori, atau nama
makanan
- Admin/Kurator: Dapat mencari makanan yang sudah ada di platform dan
mengelolanya, termasuk pengelompokan, pengeditan, dan penghapusan.
- User (Login): Bisa mencari makanan sesuai dengan kategori atau preferensi
yang telah mereka simpan.
- Fields :
  - Nama Makanan
  - Deskripsi makanan
  - Harga makanan
  - Kategori makanan
  - Gambar makanan
  - Nama restoran
  - Opsi tambah, hapus dan edit makanan
  
  Pada bagian ini yang mengerjakan : Athallah Nadhif Yuzak

3. Administrasi Makanan
   
- Admin/Kurator: Memiliki kontrol penuh untuk menambahkan makanan baru ke
platform, mengedit detail, dan memastikan kategori yang tepat.
- User (Login): Tidak memiliki akses untuk mengelola makanan
- Fields :
  - Nama Makanan
  - Deskripsi makanan
  - Harga makanan
  - Kategori makanan
  - Gambar makanan
  - Nama restoran
  - Tombol "Review" (untuk mengarahkan ke halaman ulasan)
  - Status bookmark (favorit atau tidak)
  
  Pada bagian ini yang mengerjakan : Abby Shelley Tampubolon

4. Review atau Ulasan Pengguna

- Guest (Tidak Login): Hanya bisa melihat ulasan pengguna tentang makanan, tetapi tidak bisa memberikan ulasan.
- Admin: Dapat memberikan ulasan dan rating pada makanan yang sudah ditampilkan di platform.
- User (Login): Dapat memberikan ulasan dan rating pada makanan yang sudah ditampilkan di platform.
- Fields :
  - Nama pengguna yang memberikan ulasan
  - Rating (bisa berupa bintang atau angka)
  - Teks ulasan
  - Waktu ulasan dibuat
  - Nama makanan yang diulas
  
  Pada bagian ini yang mengerjakan : Naya Kusumahayati Rachmi

5. Profile (login, register, edit profile)
   
- Guest (Tidak Login): Tidak memiliki akses ke modul profil.
- Admin/Kurator: Memiliki akses ke dashboard untuk mengelola semua makanan
yang ada di platform, mengelola kategori.
- User (Login): Hanya bisa mengedit profil pribadi, seperti nama, email, foto
- Fields :
  - Nama pengguna
  - Email pengguna
  - Password
  - Foto profil
  
  Pada bagian ini yang mengerjakan : Vico Winner Sebastian Aritonang

6. Bookmark makanan
   
- Guest (Tidak Login): Tidak bisa menandai makanan sebagai favorit.
- Admin/kurator : Dapat melihat berapa banyak bookmark yang diberikan user
pada makanan tertentu, namun tidak dapat menandai makanan sebagai favorit
sendiri.
- User (Login): Dapat menambahkan makanan ke daftar favorit atau bookmark
mereka, melihat makanan yang telah mereka tandai, dan menghapus penanda.
- Fields :
  - Daftar makanan yang ditandai sebagai favorit
  - Opsi untuk menambah dan menghapus makanan dari daftar bookmark
  - Nama makanan, harga, kategori, restoran terkait
  
  Pada bagian ini yang mengerjakan : Ammara Fasha Zia


**Sumber initial dataset**

Dataset ini diperoleh dari hasil proses pengambilan data (scraping) makanan pada aplikasi GoFood di Gojek. Hasil data yang telah kami olah ini telah melalui tahap pembersihan untuk memastikan akurasi dan kualitas informasi. Berikut adalah hasil datanya:

https://docs.google.com/spreadsheets/d/1EfaPKBR3PJBr2Co7Fe3BWvsz03EufzYwf5U5pksvyM4/edit?usp=sharing 

## link deployment ##
https://mangan-yuk-production.up.railway.app
