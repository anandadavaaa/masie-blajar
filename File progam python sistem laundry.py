import datetime

# Identitas Toko
NAMA_TOKO = "Laundry Bersih Wangi"
ALAMAT_TOKO = "Supit Urang Mojoroto No. 50, Kediri"
TELP_TOKO = "081459074528"
REKENING = "081459074528"  # nomor e-wallet & bank

# Harga layanan per kg / per item
harga_laundry = {
    "cuci_baju": 5000,
    "cuci_setrika": 8000,
    "setrika": 4000,
    "sepatu": 15000,
    "sprei": 10000,
    "selimut": 10000
}

# Voucher diskon
voucher_list = {
    "HEMAT10": 0.10,
    "CUCI20": 0.20
}

pesanan_laundry = []
nota_counter = 1


def generate_nota():
    global nota_counter
    nota = f"INV-{nota_counter:04d}"
    nota_counter += 1
    return nota


def hitung_total(layanan, berat):
    return harga_laundry[layanan] * berat


def tampilkan_header():
    print("\n==============================")
    print(" Selamat Datang di Toko Kami! ")
    print("==============================")
    print(f"Nama Toko : {NAMA_TOKO}")
    print(f"Alamat    : {ALAMAT_TOKO}")
    print(f"Telepon   : {TELP_TOKO}")
    print("==============================\n")


def tambah_pesanan():
    print("\n=== Tambah Pesanan Laundry ===")

    nama = input("Nama pelanggan: ")
    if not nama:
        print("Nama tidak boleh kosong.")
        return

    try:
        berat = float(input("Berat cucian (kg / jumlah item): "))
    except:
        print("Berat harus berupa angka.")
        return

    print("\nPilih layanan:")
    print(f"1. Cuci Baju         (Rp {harga_laundry['cuci_baju']}/kg)")
    print(f"2. Cuci + Setrika    (Rp {harga_laundry['cuci_setrika']}/kg)")
    print(f"3. Setrika Saja      (Rp {harga_laundry['setrika']}/kg)")
    print(f"4. Cuci Sepatu       (Rp {harga_laundry['sepatu']}/pasang)")
    print(f"5. Cuci Sprei        (Rp {harga_laundry['sprei']}/pcs)")
    print(f"6. Cuci Selimut      (Rp {harga_laundry['selimut']}/pcs)")
    pilihan = input("Pilih (1–6): ")

    layanan_map = {
        "1": "cuci_baju",
        "2": "cuci_setrika",
        "3": "setrika",
        "4": "sepatu",
        "5": "sprei",
        "6": "selimut"
    }

    if pilihan not in layanan_map:
        print("Pilihan tidak valid.")
        return

    layanan = layanan_map[pilihan]
    total = hitung_total(layanan, berat)

    try:
        estimasi = int(input("Estimasi selesai (hari): "))
    except:
        print("Estimasi harus berupa angka.")
        return

    express = input("Express? (10% biaya, 1 hari lebih cepat) (y/n): ")
    if express.lower() == "y":
        express_status = "Express"
        total *= 1.5
        estimasi = max(1, estimasi - 1)
    else:
        express_status = "Normal"

    voucher_code = input("Masukkan kode voucher (jika ada): ").upper()
    if voucher_code in voucher_list:
        diskon = voucher_list[voucher_code]
        total -= total * diskon
        voucher_status = f"{voucher_code} ({int(diskon * 100)}% OFF)"
    else:
        voucher_status = "-"

    antar = input("Antar–Jemput? (+5000) (y/n): ")
    if antar.lower() == "y":
        total += 5000
        antar_status = "Ya"
    else:
        antar_status = "Tidak"

    catatan = input("Catatan khusus (opsional): ")

    pembayaran = input("Metode pembayaran (cash / transfer): ")

    if pembayaran.lower() == "transfer":
        print("\n=== Metode Transfer Tersedia ===")

        print("\n--- E-WALLET ---")
        print("1. DANA")
        print("2. OVO")
        print("3. GoPay")
        print("4. ShopeePay")
        print("5. LinkAja")

        print("\n--- BANK ---")
        print("6. BCA")
        print("7. BRI")
        print("8. BNI")
        print("9. Mandiri")
        print("10. CIMB Niaga")
        print("11. SeaBank")

        pilihan_transfer = input("\nPilih nomor metode: ")

        transfer_map = {
            "1": "DANA",
            "2": "OVO",
            "3": "GoPay",
            "4": "ShopeePay",
            "5": "LinkAja",
            "6": "BCA",
            "7": "BRI",
            "8": "BNI",
            "9": "Mandiri",
            "10": "CIMB Niaga",
            "11": "SeaBank",
        }

        metode = transfer_map.get(pilihan_transfer, None)
        if metode:
            pembayaran = f"{metode} ({REKENING})"
        else:
            pembayaran = f"Transfer ({REKENING})"

    tanggal_masuk = datetime.date.today()
    tanggal_selesai = tanggal_masuk + datetime.timedelta(days=estimasi)

    pesanan = {
        "nota": generate_nota(),
        "tanggal": tanggal_masuk,
        "nama": nama,
        "berat": berat,
        "layanan": layanan,
        "express": express_status,
        "voucher": voucher_status,
        "antar": antar_status,
        "catatan": catatan,
        "bayar": pembayaran,
        "total": total,
        "status": "Menunggu",
        "estimasi": tanggal_selesai,
    }

    pesanan_laundry.append(pesanan)

    print("\nPesanan berhasil ditambahkan!")
    print_nota_lengkap(pesanan)


def print_nota_lengkap(p):
    print("\n======= NOTA LAUNDRY =======")
    print(f"{NAMA_TOKO}")
    print(f"Alamat : {ALAMAT_TOKO}")
    print(f"Telp   : {TELP_TOKO}")
    print("============================")
    print(f"Nota        : {p['nota']}")
    print(f"Tanggal     : {p['tanggal']}")
    print(f"Pelanggan   : {p['nama']}")
    print(f"Layanan     : {p['layanan']} ({p['express']})")
    print(f"Berat       : {p['berat']} kg / item")
    print(f"Voucher     : {p['voucher']}")
    print(f"Antar       : {p['antar']}")
    print(f"Catatan     : {p['catatan']}")
    print(f"Pembayaran  : {p['bayar']}")
    print(f"Estimasi    : {p['estimasi']}")
    print(f"TOTAL BAYAR : Rp {p['total']:,.0f}")
    print("============================")
    print("Terima kasih telah mencuci di sini!")
    print("Ingin kritik & saran? Hubungi WA di atas.")


def tampilkan_pesanan():
    if not pesanan_laundry:
        print("\nBelum ada pesanan.")
        return

    for p in pesanan_laundry:
        print("\n============================")
        print(f"Nota     : {p['nota']}")
        print(f"Nama     : {p['nama']}")
        print(f"Layanan  : {p['layanan']} ({p['express']})")
        print(f"Berat    : {p['berat']}")
        print(f"Total    : Rp {p['total']:,.0f}")
        print(f"Status   : {p['status']}")
        print(f"Estimasi : {p['estimasi']}")
    print("============================")


def update_status():
    nota = input("\nMasukkan nomor nota: ")
    for p in pesanan_laundry:
        if p["nota"] == nota:
            print("\nStatus baru:")
            print("1. Menunggu")
            print("2. Diproses")
            print("3. Selesai")
            pilih = input("Pilih: ")
            status_map = {"1": "Menunggu", "2": "Diproses", "3": "Selesai"}
            p["status"] = status_map.get(pilih, p["status"])
            print("Status diperbarui!")
            return
    print("Nota tidak ditemukan.")


def edit_pesanan():
    nota = input("\nMasukkan nomor nota yang mau diedit: ")
    for p in pesanan_laundry:
        if p["nota"] == nota:
            print("\nEdit data (kosongkan jika tidak diubah):")
            nama = input("Nama baru: ")
            berat = input("Berat baru: ")

            if nama:
                p["nama"] = nama
            if berat:
                try:
                    p["berat"] = float(berat)
                except:
                    print("Berat harus angka!")

            print("Pesanan diperbarui!")
            return
    print("Nota tidak ditemukan.")


def laporan_harian():
    hari = datetime.date.today()
    print(f"\n=== Laporan {hari} ===")
    for p in pesanan_laundry:
        if p["tanggal"] == hari:
            print(f"- {p['nota']} | {p['nama']} | Rp {p['total']:,.0f}")


def laporan_bulanan():
    bulan = datetime.date.today().month
    print(f"\n=== Laporan Bulan Ini ===")
    for p in pesanan_laundry:
        if p["tanggal"].month == bulan:
            print(f"- {p['nota']} | {p['nama']} | Rp {p['total']:,.0f}")


def menu():
    while True:
        print("==== SISTEM LAUNDRY ====")
        print("1. Tambah Pesanan")
        print("2. Tampilkan Pesanan")
        print("3. Edit Pesanan")
        print("4. Ubah Status")
        print("5. Laporan Harian")
        print("6. Laporan Bulanan")
        print("7. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            tambah_pesanan()
        elif pilih == "2":
            tampilkan_pesanan()
        elif pilih == "3":
            edit_pesanan()
        elif pilih == "4":
            update_status()
        elif pilih == "5":
            laporan_harian()
        elif pilih == "6":
            laporan_bulanan()
        elif pilih == "7":
            print("Terima kasih telah menggunakan layanan kami!")
            break
        else:
            print("Pilihan tidak valid.")


# HEADER HANYA SEKALI MUNCUL
tampilkan_header()
menu()