Proyek Terserah di GitHub punya dua buah repositori, yaitu

Terserah - https://github.com/hammer-code/uptoyou

Dalam catatan ini, saya akan menggunakan contoh untuk repositori Terserah saja.

Saya asumsikan bahwa Anda sudah mempunyai peralatan tempur yang dibutuhkan. Jadi, langsung saja :v

##Mempersiapkan Repositori Lokal##

Buka terminal emulator favorit Anda (Konsole, {gnome|mate}-terminal, xterm, or whatever).
Clone repositori Terserah ke repositori lokal.

$ git clone https://github.com/hammer-code/uptoyou.git

Setelah proses cloning selesai, akan muncul direktori baru, yaitu uptoyou.
Yes! Repositori lokal sudah siap :)

##Mengajukan Perubahan di Repositori Online##

Setiap kontributor punya akses ke branch master. Tapi, percayalah, jangan bermain di branch master jika tidak ingin galau dan merepotkan di kemudian hari :v

Jika Anda ingin mengubah, entah itu menambah atau mengurangi isi repositori online, manfaatkanlah fitur cantik bernama Pull Request.

[1] Buka kembali terminal emulator dan pindah ke repositori lokal.

$ cd uptoyou
[2] [Penting] Selalu refresh repositori lokal sebelum melakukan langkah selanjutnya (branching).

$ git pull
[3] Buat branch baru. Nama branch sebaiknya menggambarkan sesuatu yang ingin Anda lakukan/ajukan. Misalnya Anda ingin menambahkan dokumentasi untuk versi 1.0.9, maka branch baru yang akan Anda buat bisa dinamai dengan dokumentasi-1.0.9.

$ git checkout -b dokumentasi-1.0.9
Sebuah branch baru akan terbentuk dan otomatis Anda langsung siap bekerja di branch tersebut. Untuk memastikannya, cek daftar branch yang ada di repositori.

$ git branch
* dokumentasi-1.0.9
  master
Tanda bintang di output menandakan "tempat kerja" Anda.

[4] Lakukan perubahan (mengedit, menambah, menghapus, dsb). Setelah selesai, cek file-file yang diubah dengan perintah "git status".

$ git status
# On branch dokumentasi-1.0.9
# Changes not staged for commit:
#   (use "git add ..." to update what will be committed)
#   (use "git checkout -- ..." to discard changes in working directory)
#
#    modified:   menu/uptoyou.md
#
# Untracked files:
#   (use "git add ..." to include in what will be committed)
#
#    DOCS.html
no changes added to commit (use "git add" and/or "git commit -a")
Terlihat bahwa Anda telah memodifikasi file "menu/uptoyou.md" dan menambahkan file "DOCS.html".

Catatan: untuk menghapus file/direktori yang sudah ada sebelumnya, jangan gunakan

$ rm -rf namadirektori/
tapi

$ git rm -rf namadirektori/
sehingga perubahan tersebut nantinya bisa terekam.

[5] Pindahkan file yang telah Anda ubah ke staging area. Staging area adalah "ruang tunggu" sebelum perubahan-perubahan dimasukkan ke repositori.

$ git add menu/uptoyou.md DOCS.html
Catatan:

File-file yang dihapus dengan "git rm" otomatis akan masuk staging area.
Usahakan untuk hanya memindahkan perubahan-perubahan yang sejenis/dengan topik yang sama. Jika Anda mengubah beberapa file namun dengan topik yang berbeda, lebih baik bergantian (untuk memudahkan proses review dan koreksi).
[Penting] Usahakan untuk hanya memindahkan perubahan-perubahan yang telah Anda lakukan sendiri. Jadi, jangan lakukan
$ git add *
untuk menghindari pemindahan perubahan-perubahan yang tidak sengaja Anda lakukan.

[6] Masukkan perubahan-perubahan dari staging area ke repositori menggunakan perintah "git commit" disertai pesan commit yang sesuai.

$ git commit -m "Create help file for UPTOYOU"
[7] Lakukan perubahan-git add-git commit sesuai keinginan. Jika dirasa cukup, segera unggah branch dokumentasi-1.0.9 ke repositori online.

$ git push origin dokumentasi-1.0.9
[8] Buka repositori GitHub UPTOYOU di browser. Branch yang telah Anda unggah sebelumnya akan muncul dan siap untuk di "Pull Request". Tekan tombol hijau atau kuning entahlah saya lupa :v (deket dropdown branch). Untuk base, pilih master, sedangkan untuk compare pilih dokumentasi-1.0.9. Tekan "Turn this comparison into pull request" (or something like that). Masukkan judul dan deskripsi yang sesuai dengan perubahan yang ingin Anda ajukan, kemudian tekan "Send this pull request".

Catatan:

Kontributor tidak diperkenankan menekan tombol Close atau Merge. Closing dan merging pull request menjadi tanggung jawab maintainer. Jika Anda ingin menutup pull request, tuliskan komentar di pull request tersebut. Jadi, jangan pernah ditekan sendiri ya :p
Tips:

Perubahan yang sudah diajukan sebagai pull request masih bisa diubah lagi (misalnya ada koreksi atau penambahan). Prosesnya sama, dari nomor [4] s.d. nomor [7].
[9] Jika maintainer sudah menutup pull request (statusnya merged/closed), silakan hapus branch dokumentasi-1.0.9 di repositori lokal dengan cara berpindah dahulu ke branch master.

$ git checkout master
$ git branch -D dokumentasi-1.0.9
[10] Refresh repositori lokal

$ git pull
[11] Selesai!
