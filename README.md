PWS: https://vanessa41-footballshop.pbp.cs.ui.ac.id

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
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
- Menjalankan server Django dengan "python manage.py runserver"

- Membuat fungsi show_main di views.py untuk menampilkan nama aplikasi, nama, dan kelas. Menyiapkan data untuk ditampilkan di HTML

- Membuat folder templates yang berisi file HTML untuk menampilkan data

- Menambahkan routing di urls.py proyek dan aplikasi
Aplikasi: Buat berkas urls.py dalam direktori main dan diisi
Proyek: Buat perkas urls.py dalam direktori proyek dan tambahkan rute URL
Jalankan proyek Django dengan "python manage.py runserver"

- Membuat repository git dan melakukan deployment ke git (dengan git init, .gitignore, git remote add origin <link git>, git branch -M master, add, commit, push)
- Melakukan deployment ke PWS (menambahkan URL deployment PWS pada ALLOWED_HOSTS di settings.py, git add, commit, push perubahan ke repositori git, git push pws master)


Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Sumber: Slide 03 - MTV Django Architecture and Testing (Slide PBP)
https://drive.google.com/uc?id=1Nw8IBaTdSoQ4rxcBmlQTFPYUe2pIfkx3/view?usp=sharing

HTTP -> urls.py: Pengguna(client) mengirimkan request lewat browser. Django akan menerima request tersebut dan urls.py akan mencari routing(path) yang sesuai.
urls.py -> views.py: Setelah menemukan path yang cocok, urls.py akan mengarahkan request ke fungsi views yang sesuai. views.py mengambil data dari database lewat model.py, memproses data, dan memilih template html untuk ditampilkan ke pengguna.
views.py <-> models.py: Jika aplikasi memerlukan data dari database, views.py akan berkomunikasi dengan models.py. models.py bertugas untuk ditulis dan dibaca pada database.
html -> views.py: Setelah data siap, template html bertugas untuk menampilkan data agar terlihat lebih rapi di browser.
views.py -> HTTP: Setelah html selesai dirender, Django akan mengembalikan response ke browser dan browser akan menampilkan hasil akhir ke pengguna.

Kaitannya
- urls.py (Project): menentukan aplikasi mana yang akan menangani request
- urls.py (app): memetakan path tertentu ke fungsi di views.py
- views.py: logika aplikasi untuk memproses request, menampilkan data dari database lewat models.py dan menghubungkannya dengan template html.
- models.py: mengembalikan data ke views.py
- berkas HTML: menampilkan hasil pemrosesan data ke user client sebagai response

Fungsi utama
url menentukan ke mana permintaan (HTTP request) akan diarahkan (routing request)
model menyimpan data dan logika aplikasi
views menampilkan data dari model dan menghubungkannya dengan template html
html menentukan tampilan antarmuka pengguna


Jelaskan peran settings.py dalam proyek Django!
- File konfigurasi utama Django, yang berisi pengaturan bagaimana proyek berjalan. Setiap kali Django dijalankan, Django membaca settings.py.
Fungsi utama:
- Mengatur database
- 

- BASE_DIR: 
- DEBUG: 
- ALLOWED_HOSTS: daftar host/domain yang diizinkan mengakses project
- INSTALLED_APPS:
- DATABASES: konfigurasi database yang dipakai
- SECRET_KEY: kunci keamanan Django
- MIDDLEWARE: lapisan pengolah request/response


Bagaimana cara kerja migrasi database di Django?
makemigrations: membaca perubahan model dari models.py, membuat file migrasi di folder migrations (mempersiapkan migrasi skema model ke dalam database Django lokal)
migrate: menjalankan file migrasi dan mengupdate database sesuai model (untuk menerapkan skema model yang telah dibuat dalam database Django lokal)
Django mencatat migrasi yang sudah dijalankan agar tidak duplikat


Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
- Django full-stack framework, menyediakan fitur lengkap
- Batteries included: Admin panel otomatis, ORM, middleware, routing
- Struktur proyek jelas, cocok untuk pembelajaran dasar pengembangan software
- Komunitas besar dan dokumentasi lengkap

Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
-