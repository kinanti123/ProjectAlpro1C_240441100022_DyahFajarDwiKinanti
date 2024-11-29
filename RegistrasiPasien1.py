# Fungsi untuk membuat data pasien
def buat_pasien(id_pasien, nama, tanggal_lahir, jenis_kelamin, alamat, nomor_telepon, penyakit):
    return {
        "ID Pasien": id_pasien,
        "Nama": nama,
        "Tanggal Lahir": tanggal_lahir,
        "Jenis Kelamin": jenis_kelamin,
        "Alamat": alamat,
        "Nomor Telepon": nomor_telepon,
        "Penyakit": penyakit,
    }

# Fungsi untuk menambah pasien ke dalam sistem
def tambah_pasien(data_pasien, id_terakhir):
    nama = input("Masukkan Nama: ")
    tanggal_lahir = input("Masukkan Tanggal Lahir (DD-MM-YYYY): ")
    jenis_kelamin = input("Masukkan Jenis Kelamin (L/P): ")
    alamat = input("Masukkan Alamat: ")
    nomor_telepon = input("Masukkan Nomor Telepon: ")
    penyakit = input("Masukkan Penyakit: ")

    id_pasien_baru = id_terakhir + 1
    pasien_baru = buat_pasien(id_pasien_baru, nama, tanggal_lahir, jenis_kelamin, alamat, nomor_telepon, penyakit)
    data_pasien.append(pasien_baru)

    print(f"\nPasien berhasil didaftarkan dengan ID: {id_pasien_baru}")
    return id_pasien_baru

# Fungsi untuk menampilkan semua pasien
def tampilkan_semua_pasien(data_pasien):
    if len(data_pasien) == 0:
        print("\nTidak ada pasien yang terdaftar.")
        return

    print("\n=== Daftar Pasien Terdaftar ===")
    for pasien in data_pasien:
        tampilkan_data_pasien(pasien)

# Fungsi untuk menampilkan data pasien secara detail
def tampilkan_data_pasien(pasien):
    print("\nID Pasien:", pasien["ID Pasien"])
    print("Nama:", pasien["Nama"])
    print("Tanggal Lahir:", pasien["Tanggal Lahir"])
    print("Jenis Kelamin:", pasien["Jenis Kelamin"])
    print("Alamat:", pasien["Alamat"])
    print("Nomor Telepon:", pasien["Nomor Telepon"])
    print("Penyakit:", pasien["Penyakit"])

# Fungsi untuk mencari pasien berdasarkan ID atau penyakit
def cari_pasien(data_pasien):
    print("\nCari pasien berdasarkan:")
    print("1. ID Pasien")
    print("2. Penyakit")
    kriteria = input("Pilih opsi (1-2): ")

    if kriteria == "1":
        try:
            id_pasien = int(input("Masukkan ID Pasien: "))
            for pasien in data_pasien:
                if pasien["ID Pasien"] == id_pasien:
                    print("\n=== Data Pasien Ditemukan ===")
                    tampilkan_data_pasien(pasien)
                    return
            print("\nPasien dengan ID tersebut tidak ditemukan.")
        except ValueError:
            print("ID Pasien harus berupa angka.")

    elif kriteria == "2":
        penyakit = input("Masukkan Penyakit: ")
        ditemukan = False
        for pasien in data_pasien:
            if pasien["Penyakit"].lower() == penyakit.lower():
                if not ditemukan:
                    print("\n=== Daftar Pasien Berdasarkan Penyakit ===")
                tampilkan_data_pasien(pasien)
                ditemukan = True
        if not ditemukan:
            print("\nTidak ada pasien dengan penyakit tersebut.")
    else:
        print("Pilihan tidak valid. Coba lagi.")

# Fungsi untuk mengedit data pasien
def edit_pasien(data_pasien, id_pasien):
    pasien = next((p for p in data_pasien if p["ID Pasien"] == id_pasien), None)
    if not pasien:
        print("\nPasien dengan ID tersebut tidak ditemukan.")
        return

    print("\n=== Edit Data Pasien ===")
    nama = input(f"Nama ({pasien['Nama']}): ") or pasien["Nama"]
    tanggal_lahir = input(f"Tanggal Lahir ({pasien['Tanggal Lahir']}): ") or pasien["Tanggal Lahir"]
    jenis_kelamin = input(f"Jenis Kelamin ({pasien['Jenis Kelamin']}): ") or pasien["Jenis Kelamin"]
    alamat = input(f"Alamat ({pasien['Alamat']}): ") or pasien["Alamat"]
    nomor_telepon = input(f"Nomor Telepon ({pasien['Nomor Telepon']}): ") or pasien["Nomor Telepon"]
    penyakit = input(f"Penyakit ({pasien['Penyakit']}): ") or pasien["Penyakit"]

    pasien.update({
        "Nama": nama,
        "Tanggal Lahir": tanggal_lahir,
        "Jenis Kelamin": jenis_kelamin,
        "Alamat": alamat,
        "Nomor Telepon": nomor_telepon,
        "Penyakit": penyakit,
    })
    print("\nData pasien berhasil diperbarui.")

# Fungsi untuk menghapus data pasien
def hapus_pasien(data_pasien, id_pasien):
    pasien = next((p for p in data_pasien if p["ID Pasien"] == id_pasien), None)
    if not pasien:
        print("\nPasien dengan ID tersebut tidak ditemukan.")
        return

    data_pasien.remove(pasien)
    print("\nPasien berhasil dihapus.")

# Fungsi menu utama
def menu_utama():
    data_pasien = []
    id_terakhir = 0

    while True:
        print("\n=== Sistem Registrasi Pasien ===")
        print("1. Tambah Pasien Baru")
        print("2. Tampilkan Semua Pasien")
        print("3. Cari Pasien (ID atau Penyakit)")
        print("4. Edit Data Pasien")
        print("5. Hapus Data Pasien")
        print("6. Keluar")

        pilihan = input("Pilih opsi (1-6): ")

        if pilihan == "1":
            id_terakhir = tambah_pasien(data_pasien, id_terakhir)
        elif pilihan == "2":
            tampilkan_semua_pasien(data_pasien)
        elif pilihan == "3":
            cari_pasien(data_pasien)
        elif pilihan == "4":
            try:
                id_pasien = int(input("Masukkan ID Pasien untuk diedit: "))
                edit_pasien(data_pasien, id_pasien)
            except ValueError:
                print("ID Pasien harus berupa angka.")
        elif pilihan == "5":
            try:
                id_pasien = int(input("Masukkan ID Pasien untuk dihapus: "))
                hapus_pasien(data_pasien, id_pasien)
            except ValueError:
                print("ID Pasien harus berupa angka.")
        elif pilihan == "6":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program
menu_utama()