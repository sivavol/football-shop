# Tugas PBP
PWS: https://vanessa41-footballshop.pbp.cs.ui.ac.id


## **Tugas 2**
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Membuat folder baru untuk menempatkan proyek Django
- Membuat virtual environment dengan "python -m venv env" dan mengaktifkannya dengan "env\Scripts\activate"
Ketika terjadi error: "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process"

- Menambahkan berkas requirements.txt dan isi dengan dependencies
- Instalasi dengan "pip install -r requirements.txt"

- Membuat proyek Django dengan "django-admin startproject <nama proyek> ." untuk membuat folder awal proyek


- Membuat aplikasi bernama main pada proyek dengan "python manage.py startapp main"

- Menambahkan main ke INSTALLED_APPS di settings.py agar Django mengenali aplikasi main
- Membuat model Product dengan field sesuai ketentuan di models.py, untuk menyimpan data ke database

- Melakukan migrasi database dengan "python manage.py makemigrations" dan "python manage.py migrate"

- Membuat fungsi show_main di views.py untuk menampilkan nama aplikasi, nama, dan kelas. Menyiapkan data untuk ditampilkan di HTML

- Membuat folder templates yang berisi file HTML untuk menampilkan data

- Menambahkan routing di urls.py proyek dan aplikasi
Aplikasi: Buat berkas urls.py dalam direktori main dan diisi
Proyek: Buat berkas urls.py dalam direktori proyek dan tambahkan rute URL

- Jalankan proyek Django dengan "python manage.py runserver"

- Membuat repository git dan melakukan deployment ke git (dengan git init, .gitignore, git remote add origin <link git>, git branch -M master, add, commit, push)
- Melakukan deployment ke PWS (menambahkan URL deployment PWS pada ALLOWED_HOSTS di settings.py, git add, commit, push perubahan ke repositori git, git push pws master)


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Sumber: Slide 03 - MTV Django Architecture and Testing (Slide PBP)
https://drive.google.com/file/d/1Nw8IBaTdSoQ4rxcBmlQTFPYUe2pIfkx3/view?usp=sharing

- HTTP -> urls.py: Pengguna(client) mengirimkan request lewat browser. Django akan menerima request tersebut dan urls.py akan mencari routing(path) yang sesuai.
- urls.py -> views.py: Setelah menemukan path yang cocok, urls.py akan mengarahkan request ke fungsi views yang sesuai. views.py mengambil data dari database lewat model.py, memproses data, dan memilih template html untuk ditampilkan ke pengguna.
- views.py <-> models.py: Jika aplikasi memerlukan data dari database, views.py akan berkomunikasi dengan models.py. models.py bertugas untuk ditulis dan dibaca pada database.
- html -> views.py: Setelah data siap, template html bertugas untuk menampilkan data agar terlihat lebih rapi di browser.
- views.py -> HTTP: Setelah html selesai dirender, Django akan mengembalikan response ke browser dan browser akan menampilkan hasil akhir ke pengguna.

Kaitannya
- urls.py (Project): menentukan aplikasi mana yang akan menangani request
- urls.py (app): memetakan path tertentu ke fungsi di views.py
- views.py: logika aplikasi untuk memproses request, menampilkan data dari database lewat models.py dan menghubungkannya dengan template html.
- models.py: mengembalikan data ke views.py
- berkas HTML: menampilkan hasil pemrosesan data ke user client sebagai response

Fungsi utama
- url menentukan ke mana permintaan (HTTP request) akan diarahkan (routing request)
- model menyimpan data dan logika aplikasi
- views menampilkan data dari model dan menghubungkannya dengan template html
- html menentukan tampilan antarmuka pengguna


3. Jelaskan peran settings.py dalam proyek Django!
- File konfigurasi utama Django, yang berisi pengaturan bagaimana proyek berjalan, menentukan cara kerja keseluruhan sistem (seperti database dan keamanan). Setiap kali Django dijalankan, Django membaca settings.py.

Fungsi utama:
- Mengatur database
- Menentukan aplikasi yang terdaftar
- Menentukan security settings
- Mengatur middleware dan pengaturan request/response
- Menentukan domain/host yang diizinkan

- BASE_DIR: lokasi folder utama proyek
- DEBUG: menampilkan error saat ada bug
- ALLOWED_HOSTS: daftar host/domain yang diizinkan mengakses proyek
- INSTALLED_APPS: daftar aplikasi yang digunakan di proyek
- DATABASES: konfigurasi database yang dipakai
- SECRET_KEY: kunci keamanan Django
- MIDDLEWARE: lapisan yang memproses request dan response


4. Bagaimana cara kerja migrasi database di Django?
Django menggunakan migrasi untuk mengelola perubahan struktur database secara otomatis dan terkontrol. makemigrations membuat file instruksi perubahan, sedangkan migrate menerapkan instruks tersebut ke database.

- makemigrations: membaca perubahan model dari models.py, membuat file migrasi di folder migrations. File ini belum mengubah database, hanya berisi instruksi perubahan. (untuk mempersiapkan migrasi skema model ke dalam database Django lokal)
- migrate: menjalankan file migrasi yang sudah dibuat, mengupdate database lokal agar sesuai dengan model, Django mencatat migrasi yang dijalankan sehingga setiap perubahan dapat dilihat. (untuk menerapkan skema model yang telah dibuat dalam database Django lokal)


5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
- Django full-stack framework, menyediakan fitur lengkap untuk membuat website, mulai dari front-end hingga back-end, sehingga pemula tidak perlu memperlajari dua framework terpisah.
- Struktur proyek yang jelas, cocok untuk pembelajaran dasar pengembangan aplikasi yang terstruktur dengan menggunakan pendekatan MTV (Model, Template, View) yang memisahkan logika aplikasi, user interface, dan data.
- Database menggunakan sintaks Python sehingga membuat kode lebih mudah dibaca dan di maintenance.
- Memiliki fitur keamanan bawaan untuk melindungi dari serangan umum, sehingga pemula dapat belajar membangun aplikasi yang aman tanpa harus memahami detail keamanan dari awal.
- Memiliki banyak fitur bawaan, sehingga pemula tidak perlu mengonfigurasi banyak hal dari awal.

Django dapat dipilih untuk pembelajaran awal karena lengkap, aman, dan terstruktur, sehingga pemula dapat fokus memahami konsep dasar pengembangan dengan baik tanpa terbebani dengan konfigurasi teknis yang rumit.

Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
- Tidak ada

Sumber:
https://www.geeksforgeeks.org/python/django-settings-file-step-by-step-explanation/
https://www.revou.co/kosakata/django



## **Tugas 3**

### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
 - Data delivery merupakan proses pengiriman data dari satu bagian sistem ke bagian lainnya, bisa dari server ke client maupun client ke server, agar data dapat diproses atau ditampilkan. Contoh, add product merupakan deliver data dari client ke server untuk disimpan dalam database. detail product merupakan deliver data dari server ke client, untuk ditampilkan.

 - Client bertugas untuk menampilkan data ke pengguna, server untuk mengelola data dan menangani request dari client, dan database untuk menyimpan data. Ketiga ini membutuhkan data delivery agar komunikasi antar bagian dapat berjalan (untuk mengirim dan menerima data) dengan format yang terstruktur seperti HTML, XML, atau JSON.

 - Tanpa data delivery, setiap komponen ini tidak dapat saling terhubung, platform tidak dapat mengelola data-data antar komponen dengan baik. Data delivery penting sebagai jembatan yang memungkinkan komunikasi lancar antara berbagai bagian dari sistem, seperti client, server, dan database.

### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
- JSON memiliki format yang ringkas dan sederhana. Data ditulis dalam bentuk pasangan key-value yang mirip dengan struktur dictionary di Python. Struktur ini membuat JSON lebih mudah dipahami oleh pengembang, ringan, dan lebih cepat untuk diproses oleh mesin. JSON juga membutuhkan lebih sedikit ruang penyimpanan dibandingkan XML, yang membuat proses transfer data menjadi lebih cepat dan efisien.

- Di sisi lain, XML menggunakan tag untuk membungkus setiap elemen datanya. Struktur XML lebih fleksibel dibandingkan JSON karena dapat menyimpan data yang lebih kompleks sehingga sering digunakan pada proyek besar. Namun, fleksibilitas ini menyebabkan ukuran file XML cenderung lebih besar karena penggunaan tag yang banyak, dan proses XML juga lebih lambar dibandingkan JSON.

- JSON lebih populer karena kesederhanaannya, kemudian pembacaan, ukuran yang lebih kecil, serta performa lebih cepat. Ini membuat JSON menjadi pilihan untuk aplikasi berbasis web maupun mobile. Meskipun demikian, XML tetap memiliki tempatnya, terutama pada sistem besar yang memiliki struktur data yang kompleks dan fleksibel.
 
### Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
 - Method is_valid() pada form berfungsi untuk memvalidasi data yang dimasukkan pengguna sebelum akhirnya data diproses atau disimpan dalam database.

 - Ketika sebuah form dikirimkan, data yang dimasukkan akan diperiksa oleh is_valid(). Proses ini memerikda setiap field dalam data form, memastikan bahwa data yang dimasukkan sesuai dengan tipe data yang diharapkan dan memenuhi semua aturan validasi yang telah ditentukan di model atau form itu sendiri.

 - Jika data valid, method akan mengembalikan nilai True, data pada form akan diproses dan disimpan dalam database. Namun jika data tidak valid, form akan ditampilkan kembali kepada pengguna bersama dengan pesan error yang jelas, sehingga pengguna dapat memperbaiki input mereka.
 
 - Dengan adanya mekanisme ini, Django membantu untuk mencegah data yang dimasukkan salah masuk ke dalam database dan menghindari error, menjaga integritas sistem, juga meningkatkan keamanan dan kebersihan database.

### Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
 - Django menyediakan csrf_token sebagai keamanan untuk mencegah mencegah CSRF Attack(Cross-Site Request Forgery). CSRF adalah serangan di mana penyerang mencoba memanfaatkan pengguna yang sudah terautentikasi atau login untuk mengirimkan request berbahaya ke server tanpa sepengetahuan mereka.

 - Ketika server meminta form tersebut, Django akan memverifikasi token, mengecek kevalidan request untuk memastikan bahwa request tersebut benar-benar berasal dari sumber yang sah dan bukan dari pihak luar yang berusaha menyerang. Request akan ditolak jika token tidak valid.

 - Dengan tidak adanya scrf_token, aplikasi menjadi tidak aman dan rentan terhadap serangan CSRF. Penyerang dapat membuat halaman palsu yang terlihat seperti halaman resmi, yang kemudian memanfaatkan akun pengguna yang sedang login untuk melakukan tindakan berbahaya seperti mengubah data, menghapus data, ataupun melakukan transaksi.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.

  - Pada models.py:
    - Tambahkan field id
    - Lakukan migration untuk mengupdate models

  - Pada file views.py:
    - from django.http import HttpResponse
    - from django.core import serializers
    - import models Porduct yang digunakan pada fungsi untuk melihat objek
    - buat 4 fungsi views dengan try except untuk mengantisipasi id tidak ditemukan


- Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 1.
    - Pada file urls.py pada direktori main:
        - import 4 fungsi yang sudah dibuat
        - tambahkan path url ke dalam url patterns untuk akses fungsi yang sudah diimpor


- Implementasi skeleton sebagai kerangka views (membuat base.html)
    - Buat direktori "templates" di root folde dan berkas "base.html" untuk kerangka umum.
    - Di settings.py pada variable TEMPLATES, ditambahkan potongan code DIRS untuk mendeteksi base.html di berkas "template" di root directory. DIRS berisi seluruh list direktori, folder mana saja untuk dicari file template dengnan urutan folder dalma list menentukan prioritas pencarian template. (Tugas sebelumnya tidak membutuhkan DIRS karena template berada dalam app/main, Django secara default mencari hanya di dalam app. Sehingga pada tugas 3 ini, ketika ditambahkan base.html di templates pada root project(di luar app), kita perlu menambahkan DIRS agar Django dapat mendeteksi folder global untuk template).
    - Menambah block content dan extend base.html di file main.html untuk dijadikan template utama

- Menambahkan tombol "Add" direct ke form add product dan tombol "Detail" direct ke form detail product
    - Menambahkan context untuk product list di fungsi show_main di views.py untuk main.html dapat menunjukkan list product
    - Mengubah berkas main.html menambahkan button dan url nya menuju function di views.py

- Buat file "forms.py" di direktori "main". Import ModelForm, class bawaan yang memudahkan buat form dari model. Form akan berdasarkan struktur model ini, otomatis buat field input dan validasi otomatis sesuai tipe data di model. ProductForm sebagai jembatan otomatis antara form HTML dan model database Product

    - Tambah fungsi di views.py untuk add product dan show detail, dan ngedirect ke file html yang sesuai.
        - Fungsi add_product menggunakan form yang udah dibuat sebelumnya, dan bisa langsung di save, dengan form.save() akan langsung tersimpan ke database
        - Fungsi show_detail akan mencoba mencari object yang sesuai dengan id pada data produk, jika tidak ditemukan akan memberikan error 404 Not Found. Jika ditemukan, maka objek produk dikembalikan. Lalu membuat context yang isinya berupa objek produk yang diambil dari database, yang dimana nantinya pada product_detail.html bisa diakses data productnya.


- Membuat halaman form untuk menambahkan objek model pada app sebelumnya.
    - Buat file add_product.html untuk halaman form add product
    - Isi sesuai dengan yang diinginkan
        - Form mengirimkan data ke server menggunakan metode POST karena mengubah data
        - Menambahkan token keamanan, diperlukan ketika membuat form POST
        - form.as_table, Django otomatis merender seluruh field form (PorductForm) dalam bentuk table rows dan setiap field akan punya label dan input.

- Membuat halaman yang menampilkan detail dari setiap data objek model.
    - Membuat product_detail.html untuk halaman form detail product
    - Isi sesuai dengan yang diinginkan

- Tambahkan entri url pws pada CSRF_TRUSTED_ORIGINS di settings.py. CSRF_TRUSTED_ORIGINS berisi daftar URL yang dianggap aman untuk menerima request seperti POST (mengizinkan domain luar untuk mengirimkan form). Digunakan jika proyek diakses dari domain eksternal atau server deployment, tidak pada local host.

### Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
https://docs.google.com/document/d/1NJP6V4iPBpmWb_cuJqhu4gwz8LW48pW49eaBW3HsTcw/edit?usp=sharing


### Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Tidak ada

References:
https://localstartupfest.lokercepat.id/faq/perbedaan-xml-dan-json/
https://docs.djangoproject.com/en/5.2/topics/forms/
https://owasp.org/www-community/attacks/csrf







## **Tugas 4**
### Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
-  Form bawaan Django yang digunakan untuk menangani proses login/autentikasi pengguna. Form ini merupakan bagian dari sistem autentikasi Django (django.contrib.auth.forms) yang menyediakan fungsionalitas standar untuk memverifikasi pengguna. Menyediakan field standard username dan password yang kemudian akan dilakukan validasi dengan autentikasi django, dan mengembalikan objek User jika valid. Username untuk identifikasi dan password untuk verifikasi.
- Kelebihan: melakukan validasi otomatis, fleksibel dapat menambahkan field tambahan, menyediakan pesan error jika input tidak valid.
- Kekurangan: default hanya menggunakan/menangani username dan password, sehingga butuh pengembangan tambahan untuk kebutuhan yang kompleks.

### Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
- Autentikasi:
    - Proses memvalidasi/memverifikasi identitas pengguna yang ingin login (username dan password yang dimasukkan sesuai dengan database) 
    - Pengimplimentasiannya dapat dilakukan dengan melakukan import django.contrib.auth, khususnya authenticate().
- Otorisasi: 
    - Proses menentukan permissions atau akses apa yang dapat dilakukan oleh pengguna ketika login. Memberikan izin pengguna yang sudah terautentikasi untuk mengakses fungsi-fungsi tertentu.
    - Pengimplementasiannya 
- Django memiliki sistem autentikasi bawaan yang dapat diimport yaitu django.contrib.auth, menyediakan fitur autentikasi dan otorisasi.

### Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
HTTP secara default bersifat stateless, artinya setiap browser mengirimkan request, request ini akan bersifat independent, tidak diketahui oleh server darimana request ini berasal dan hubungan dengan request sebelumnya. Session dan cookies ditambahkan agar web bisa mengingat user/pengirim yang sama dari satu halaman ke halaman lainnya.
- Session:
    - Data yang disimpan pada sisi server untuk menyimpan data yang lebih sensitif, seperti informasi login. Browser hanya menyimpan cookie khusus yang berisi suatu session ID ke server pada setiap pengguna setelah berhasil melakukan login untuk dapat menghubungkan pengguna dengan data session di server. Dengan ini, data lebih aman karena tidak tersimpan langsung di browser.
    - Kelebihan session adalah keamanan lebih tinggi untuk menyimpan informasi mengenai pengguna, karena disimpan di server, tidak dapat disalahgunakan oleh yang lain dan bisa untuk menyimpan data yang besar dan kompleks. Namun kekurangannya, beban server tinggi karena semua state disimpan pada server.
- Cookies:
    - Data yang disimpan pada sisi klien/browser. Berisi data dalam bentuk pasangan key-value yang dikirimkan ke server setiap kali pengguna melakukan request. Misalnya, cookie dapat digunakan untuk menyimpan preferensi bahasa, data login sederhana, atau pengaturan tampilan.
    - Kelebihan cookies adalah bersifat sederhana dan tidak membebani server sehingga cepat. Cocok untuk data ringan dan non-sensitif. Kekurangannya adalah data kurang aman karena disimpan di browser sehingga dapat dengan mudah dimanipulasi dan juga hanya dapat menyimpan maksimal 4KB data.

### Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
- Cookies menyimpan preferensi pengguna dan informasi login, sehingga meningkatkan pengalaman pengguna.
- Namun tidak sepenuhnya aman, karena cookies menyimpan informasi penting seperti user sessions dan juga data tracking. Hal ini membuat cookies rentan jika tidak dikonfigurasi dengan baik.
- Risiko utama cookies adalah ketika dipakai untuk tracking lintas situs atau menyimpan data sensitif, karena bisa menyebabkan kebocoran privasi dan penyalahgunaan data.

- Risiko potensial yang harus diwaspadai:
    - Risiko privasi: tracking tanpa consent user
    - Data misuse: potensi penyalahgunaan data browsing habits
    - Cross-site tracking: bisa melacak aktivitas across different websites.

- Penanganan Django:
    - Django menggunakan cookies hanya untuk autentikasi dan session management (user session), bukan untuk menyimpan data sensitif langsung
    - Menyediakan fitur bawaan untuk mengamankan cookies melalui konfigurasi seperti hanya menggunakan HTTPS dan melindungi dari serangan CSRF(SESSION_COOKIE_SECURE dan SESSION_COOKIE_HTTPONLY) untuk mencegah pencurian data.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya.
    - Register:
        - Import UserCreationFOrm dan messages pada views.py
        - Membuat fungsi register yang secara otomatis membuat akun pengguna ketika form di submit, setelah itu di-redirect ke register.html
        - Buat berkas register.html di main/templates sesuai keinginan
        - Pada url.py, import dan tambahkan path url untuk akses fungsi register
    - Login:
        - Import authentication form, authenticate, dan login
        - Membuat fungsi login yang berfungsi untuk melakukan autentikasi pengguna yang login, setelah berhasil akan di-redirect ke login.html
        - Buat berkas login.html di main/templates sesuai keinginan
        - Pada urls.py import dan tambahkan path url untuk akses fungsi login
    - Logout:
        - Import logout
        - Membuat fungsi logout untuk proses keluar dari sesi yang sedang dijalankan
        - Tambahkan tombol pada main.html yang mengarah ke url logout.
        - Pada urls.py import dan tambahkan path url untuk akses fungsi logout

    - Merestriksi akses halaman main dan product detail, sehingga hanya dapat ditampilkan ketika pengguna sudah login.
        - Menambahkan decorator login_required di atas fungsi show_main dan show_product.
            - Format: login_required(redirect_field_name='next', login_url=None).
            - Sehingga ketika user tidak login, akan redirect ke login url terlebih dahulu. Ketika sudah terlogin baru akan mengeksekusi fungsi dibawah decorator tersebut.

- Menghubungkan model Product dengan User.
    - Pada models.py, import User dan menambahkan potongan code ForeignKey untuk menghubungkan satu product dengan satu user melalui sebuah relationship.
    - Melakukan file migrasi untuk mengupdate perubahan pada models.py (makemigrations dan migrate)
    - Pada views.py, mengubah potongan code pada fungsi add_product dengan menambahkan commit False sebagai parameter form.save, agar ketika product ditambahkan, form tidak hanya langsung menyimpan data product yang ditambahkan, tetapi juga dapat menyimpan user yang sedang login dengan nilai request.user.

    - Pada views.py, menambah potongan code untuk dapat memfilter tampilan product yang diinginkan (mengambil nilai parameter filter jika ada) dengan default awal menampilkan semua product (default ke "all")
    - Pada main.html, menambahkan button My Product dan All Product beserta dengan filter sehingga dapat diidentifikasi oleh fungsi show_main untuk memfilter dan menampilkan product yang sesuai.
        - Perlu ditambahkan jenis type pada button, karena default type merupakan submit (mengirim form ketika ditekan). Sehingga diperlukan type button jika tidak ada yang ingin dilakukan. Aksi klik button di-handle oleh <a>.
    
    - Menampilkan user yang memiliki product pada halaman product detail dengan menambahkan kode pada product_detail.html untuk mengambil mengambil username pada field user yang didapatkan berdasarkan product.


- Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi.
    - Cookies dapat dimanfaatkan untuk membedakan setiap pengguna dengan datanya masing-masing.
    - Pengimplementasian pertama dilakukan dengan import datetime untuk mengetahui last login, from django.http import HttpResponse dan HttpResponseRedirect, dan from django.urls import reverse.
    - Memodifikasi fungsi login dengan variabel response agar dapat menyimpan waktu terakhir pengguna login dan ketika berhasil login akan otomatis akan membawa user ke halaman utama (show_main).
    - Menambahkan key last login dan valuenya pada fungsi show_main dengan method .get(). Jika cookie last login tidak ada, akan mengirimkan default "Never".
    - Pada fungsi logout juga perlu dimodifikasi untuk menghapus cookie last_login sehingga data waktu login sebelumnya hilang.

    - Menampilkan detail informasi username dan last login dengan menambahkan potongan kode pada main.html, tambah informasi username login dan last login

- Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal.


References:
https://docs.djangoproject.com/en/5.2/topics/auth/default/
https://www.geeksforgeeks.org/websites-apps/understanding-cookies-in-web-browsers/

## **Tugas 5**

### Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Ketika terdapat beberapa CSS selector yang berlaku untuk satu elemen HTML, browser akan menentukan style yang digunakan berdasarkan CSS Specifity Rules, dengan urutan prioritasnya adalah:
1. **Inline Style**
- Selector ini memiliki prioritas tertinggi dan langsung diaplikasikan menggunakan atribut style.
2. **ID Selector**
- Prioritas tertinggi kedua, setelah inline style. Diidentifikasi menggunakan atribut id.
3. **Class and Pseudo-classes**
- Selector ini berada pada posisi ketiga, biasanya digunakan pada nama class maupun pseudo-classes.
4. **Attributes**
- Biasanya digunakan pada atribut-atribut html.
5. **Element dan Pseudo-elements**
- Selector dengan posisi terendah, yang biasa digunakan pada elemen-elemen dan pseudo-element dari HTML.

### Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
Responsive design adalah pendekatan desain web agar tampilan halaman dapat menyesuaikan ukuran layar atau dimensi perangkat yang digunakan. Sehingga tampilan di HP dapat berbeda dengan tampilan di tablet ataupun desktop. Konsep ini penting karena dapat meningkatkan user experience di berbagai perangkat, membuat website lebih aksesibel, dan mengurangi kebutuhan membuat aplikasi berbeda untuk tiap perangkat.

Aplikasi-aplikasi yang sudah reponsive seperti YouTube, video dan tampilan homepage menyesuaikan ukuran layar. Selain itu, terdapat contoh lain seperti Instagram, LinkedIn, dan masih banyak aplikasi lain yang responsive yang dapat kita temukan pada website yang kita gunakan sehari-hari. Contoh aplikasi yang belum menerapkan responsive design adalah SIAKNG. Dapat dilihat ketika menggunakan SIAKNG melalui smartphone, tampilannya masih merupakan tampilan browser yang sama seperti saat membukanya melalui perangkat laptop, dan ini menyebabkan ketidaknyamanan ketika menggunakannya melalui perangkat mobile.
 
### Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
- Margin: jarak diluar elemen, memisahkan elemen lain. Dapat mengatur margin sisi atas, bawah, kanan, dan kiri dari elemen yang diinginkan.
- Border: garis yang mengelilingi elemen untuk memberikan batas yang dapat dilihat pengguna, berada di antara margin dan padding. Border dapat dikustomisasi, baik garis, warna, maupun stylenya.
- Padding: jarak/ruang yang berada di dalam elemen, antara konten dengan border. Sama seperti margin, padding juga dapat digunakan untuk berbagai sisi elemen.


### Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flexbox (Flexible Box Layout): 
- Digunakan untuk mengatur layout satu dimensi (baris atau kolom)
- Memudahkan dalam mengatur ruang dan elemen dalam suatu kontainer secara otomatis. Fleksibel dalam mengatur posisi, ukuran, dan spasi antar elemen
- Cocok untuk navigasi, toolbar, atau list card horizontal

Grid layout:
- Digunakan untuk mengatur layout dua dimensi (baris dan kolom), sehingga memungkinkan pengaturan baris serta kolom sekaligus.
- Memberikan kontrol penuh untuk membuat tata letak kompleks. Memudahkan dalam mengatur ruang serta elemen ketika bekerja dalam suatu grid
- Cocok untuk dashboard, layout halaman, atau layout majalah.


### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
- Implementasikan fungsi untuk menghapus dan mengedit product.
    - Mengedit product
        - Buat fungsi edit_product di views dengan parameter request dan id product.
            - Mendapatkan product by Id
            - Membuat forms
            - Jika valid, form akan di save dan redirect ke halaman awal. Kalau tidak valid, tetap di halaman edit product.
        - Buat berkas edit_product.html sebagai tampilan form edit
        - Menambahkan url path untuk mengakses fungsi yang sudah dibuat
    
    - Menghapus product
        - Buat fungsi delete_product di views dengan parameter request dan id product untuk menghapus product yang didapatkan by Id. **Setelahnya, return HttpsResponseRedirect(reverse('main:show_main'))**
        - Menambahkan url path untuk mengakses fungsi yang sudah dibuat


- Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma)

    - Menambahkan script tailwind pada base.html
    - Konfigurasi static files pada aplikasi dengan menambahkan potongan kode di setting.py

    - Membuat file global.css di /static/css pada root directory dan menambahkan custom styling.
    - Menghubungkan global.css dan menambahkan script tailwind ke base.html dengan memodifikasi berkas base.html. Menambahkan script dan link.

    - Kustomisasi halaman login, register, tambah product, edit product, dan detail product semenarik mungkin.
        - Mengedit login.html, register.html, add_product.html, product_detail.html.

    - Kustomisasi halaman daftar product menjadi lebih menarik dan responsive. Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar. Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card (tidak boleh sama persis dengan desain pada Tutorial!).
        - Menambahkan berkas card_product.html untuk tampilan card
        - Menambahkan image ke static/image sebagai tampilan ketika tidak ada thumbnail
        - Mengedit main.html untuk menggunakan card product dan image.


    - Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!

    - Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.
        - Buat berkas navbar.html pada folder templates di root directory.
        - Include navbar.html pada main.html

References:
https://www.geeksforgeeks.org/css/css-specificity/


## **Tugas 6**
### Apa perbedaan antara synchronous request dan asynchronous request?
### Bagaimana AJAX bekerja di Django (alur request–response)?
### Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
### Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
### Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
</details>

