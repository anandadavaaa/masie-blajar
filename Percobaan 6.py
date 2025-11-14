import datetime

# Daftar layanan laundry
layanan = {
    1: {"nama": "Cuci Kering", "harga": 5000},
    2: {"nama": "Cuci Setrika", "harga": 8000},
    3: {"nama": "Setrika Saja", "harga": 4000},
    4: {"nama": "Cuci Express (4 jam)", "harga": 12000},
}

total_pemasukan = 0   # menyimpan total uang hasil laundry


# Menampilkan layanan
def tampilkan_layanan():
    print("\n=== Daftar Layanan Laundry ===")
    for id_layanan, data in layanan.items():
        print(f"{id_layanan}. {data['nama']} - Rp{data['harga']}/kg")


# Hitung biaya
def hitung_biaya(jenis, berat):
    harga_per_kg = layanan[jenis]["harga"]
    return harga_per_kg * berat


# Simpan transaksi
def simpan_transaksi(nama, layanan_txt, berat, total):
    with open("transaksi_laundry.txt", "a") as f:
        waktu = datetime.datetime.now()
        f.write(f"\n=== Transaksi ({waktu}) ===\n")
        f.write(f"Pelanggan: {nama}\n")
        f.write(f"Layanan: {layanan_txt}\n")
        f.write(f"Berat: {berat} kg\n")
        f.write(f"Total: Rp{total}\n")
    print("✔ Transaksi disimpan!")


# Program utama
while True:
    print("\n===== SmartLaundry =====")
    print("1. Lihat Layanan")
    print("2. Laundry Baru")
    print("3. Lihat Total Pemasukan")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tampilkan_layanan()

    elif pilihan == "2":
        nama = input("\nNama pelanggan: ")
        tampilkan_layanan()

        jenis = int(input("Pilih nomor layanan: "))
        if jenis not in layanan:
            print("❌ Layanan tidak ditemukan!")
            continue

        berat = float(input("Masukkan berat (kg): "))
        total = hitung_biaya(jenis, berat)

        print("\n=== Struk Laundry ===")
        print(f"Pelanggan : {nama}")
        print(f"Layanan   : {layanan[jenis]['nama']}")
        print(f"Berat     : {berat} kg")
        print(f"Total     : Rp{total}")

        # Tambahkan pemasukan
        total_pemasukan += total

        # Simpan transaksi
        simpan_transaksi(nama, layanan[jenis]["nama"], berat, total)

    elif pilihan == "3":
        print(f"\n💰 Total pemasukan Laundry: Rp{total_pemasukan}")

    elif pilihan == "4":
        print("Terima kasih telah menggunakan SmartLaundry!")
        break

    else:
        print("❌ Pilihan tidak valid!")