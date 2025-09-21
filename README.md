PWS: https://vanessa41-footballshop.pbp.cs.ui.ac.id

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



# **Tugas 3**

## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
 - Data delivery merupakan proses pengiriman data dari satu bagian sistem ke bagian lainnya, bisa dari server ke client maupun client ke server, agar data dapat diproses atau ditampilkan. Contoh, add product merupakan deliver data dari client ke server untuk disimpan dalam database. detail product merupakan deliver data dari server ke client, untuk ditampilkan.

 - Client bertugas untuk menampilkan data ke pengguna, server untuk mengelola data dan menangani request dari client, dan database untuk menyimpan data. Ketiga ini membutuhkan data delivery agar komunikasi antar bagian dapat berjalan (untuk mengirim dan menerima data) dengan format yang terstruktur seperti HTML, XML, atau JSON.

 - Tanpa data delivery, setiap komponen ini tidak dapat saling terhubung, platform tidak dapat mengelola data-data antar komponen dengan baik. Data delivery penting sebagai jembatan yang memungkinkan komunikasi lancar antara berbagai bagian dari sistem, seperti client, server, dan database.

## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
- JSON memiliki format yang ringkas dan sederhana. Data ditulis dalam bentuk pasangan key-value yang mirip dengan struktur dictionary di Python. Struktur ini membuat JSON lebih mudah dipahami oleh pengembang, ringan, dan lebih cepat untuk diproses oleh mesin. JSON juga membutuhkan lebih sedikit ruang penyimpanan dibandingkan XML, yang membuat proses transfer data menjadi lebih cepat dan efisien.

- Di sisi lain, XML menggunakan tag untuk membungkus setiap elemen datanya. Struktur XML lebih fleksibel dibandingkan JSON karena dapat menyimpan data yang lebih kompleks sehingga sering digunakan pada proyek besar. Namun, fleksibilitas ini menyebabkan ukuran file XML cenderung lebih besar karena penggunaan tag yang banyak, dan proses XML juga lebih lambar dibandingkan JSON.

- JSON lebih populer karena kesederhanaannya, kemudian pembacaan, ukuran yang lebih kecil, serta performa lebih cepat. Ini membuat JSON menjadi pilihan untuk aplikasi berbasis web maupun mobile. Meskipun demikian, XML tetap memiliki tempatnya, terutama pada sistem besar yang memiliki struktur data yang kompleks dan fleksibel.
 
## Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
 - Method is_valid() pada form berfungsi untuk memvalidasi data yang dimasukkan pengguna sebelum akhirnya data diproses atau disimpan dalam database.

 - Ketika sebuah form dikirimkan, data yang dimasukkan akan diperiksa oleh is_valid(). Proses ini memerikda setiap field dalam data form, memastikan bahwa data yang dimasukkan sesuai dengan tipe data yang diharapkan dan memenuhi semua aturan validasi yang telah ditentukan di model atau form itu sendiri.

 - Jika data valid, method akan mengembalikan nilai True, data pada form akan diproses dan disimpan dalam database. Namun jika data tidak valid, form akan ditampilkan kembali kepada pengguna bersama dengan pesan error yang jelas, sehingga pengguna dapat memperbaiki input mereka.
 
 - Dengan adanya mekanisme ini, Django membantu untuk mencegah data yang dimasukkan salah masuk ke dalam database dan menghindari error, menjaga integritas sistem, juga meningkatkan keamanan dan kebersihan database.

## Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
 - Django menyediakan csrf_token sebagai keamanan untuk mencegah mencegah CSRF Attack(Cross-Site Request Forgery). CSRF adalah serangan di mana penyerang mencoba memanfaatkan pengguna yang sudah terautentikasi atau login untuk mengirimkan request berbahaya ke server tanpa sepengetahuan mereka.

 - Ketika server meminta form tersebut, Django akan memverifikasi token, mengecek kevalidan request untuk memastikan bahwa request tersebut benar-benar berasal dari sumber yang sah dan bukan dari pihak luar yang berusaha menyerang. Request akan ditolak jika token tidak valid.

 - Dengan tidak adanya scrf_token, aplikasi menjadi tidak aman dan rentan terhadap serangan CSRF. Penyerang dapat membuat halaman palsu yang terlihat seperti halaman resmi, yang kemudian memanfaatkan akun pengguna yang sedang login untuk melakukan tindakan berbahaya seperti mengubah data, menghapus data, ataupun melakukan transaksi.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
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

## Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
https://docs.google.com/document/d/1NJP6V4iPBpmWb_cuJqhu4gwz8LW48pW49eaBW3HsTcw/edit?usp=sharing


## Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Tidak ada

References:
https://localstartupfest.lokercepat.id/faq/perbedaan-xml-dan-json/
https://docs.djangoproject.com/en/5.2/topics/forms/
https://owasp.org/www-community/attacks/csrf







# **Tugas 4**
## Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.

## Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?

## Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya.
    - Register:
        - Membuat fungsi register, render ke register.html
        - Buat berkas register.html di main/templates sesuai keinginan
        - Pada url.py, import dan tambahkan path url untuk akses fungsi register
    - Login:
        - Membuat fungsi login, render ke login.html
        - Buat berkas login.html di main/templates sesuai keinginan
        - Pada urls.py import dan tambahkan path url untuk akses fungsi login
    - Logout:
        - Membuat fungsi logout
        - Tambahkan tombol pada main.html yang mengarah ke url logout.

    - Merestriksi akses halaman main dan product detail, sehingga hanya dapat ditampilkan ketika pengguna sudah login.
        - Menambahkan decorator login_required di atas fungsi show_main dan show_product.
            - Format: login_required(redirect_field_name='next', login_url=None).
            - Sehingga ketika user tidak login, akan redirect ke login url terlebih dahulu. Ketika sudah terlogin baru akan mengeksekusi fungsi dibawah decorator tersebut.

- Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal.

- Menghubungkan model Product dengan User.
    - Pada models.py, import User dan menambahkan potongan code ForeignKey untuk menghubungkan satu product dengan satu user melalui sebuah relationship.
    - Melakukan file migrasi untuk mengupdate perubahan pada models.py (makemigrations dan migrate)
    - Pada views.py, mengubah potongan code pada fungsi add_product dengan menambahkan commit False sebagai parameter form.save, agar ketika product ditambahkan, form tidak hanya langsung menyimpan data product yang ditambahkan, tetapi juga dapat menyimpan user yang sedang login dengan nilai request.user.

    - Pada views.py, menambah potongan code untuk dapat memfilter tampilan product yang diinginkan (mengambil nilai parameter filter jika ada) dengan default awal menampilkan semua product (default ke "all")
    - Pada main.html, menambahkan button My Product dan All Product beserta dengan filter sehingga dapat diidentifikasi oleh fungsi show_main untuk memfilter dan menampilkan product yang sesuai.
        - Perlu ditambahkan jenis type pada button, karena default type merupakan submit (mengirim form ketika ditekan). Sehingga diperlukan type button jika tidak ada yang ingin dilakukan. Aksi klik button di-handle oleh <a>.
    
    - Menampilkan user yang memiliki product pada halaman product detail dengan menambahkan kode pada product_detail.html untuk mengambil mengambil username pada field user yang didapatkan berdasarkan product.


- Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi.
    - Cookies
    - main.html tambah informasi username login dan last login


References:
https://docs.djangoproject.com/en/5.2/topics/auth/default/
</details>

