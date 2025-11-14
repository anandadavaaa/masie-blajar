import random

print("=== GAME TEBAK ANGKA ===")
print("Saya sudah memilih angka dari 1 sampai 100.")
print("Coba tebak!")

# komputer memilih angka
angka_rahasia = random.randint(1, 100)
percobaan = 0

while True:
    try:
        tebakan = int(input("Masukkan tebakanmu: "))
        percobaan += 1

        if tebakan < angka_rahasia:
            print("Terlalu kecil! Coba lagi.\n")
        elif tebakan > angka_rahasia:
            print("Terlalu besar! Coba lagi.\n")
        else:
            print(f"🎉 Benar! Angkanya adalah {angka_rahasia}.")
            print(f"Kamu menebak dalam {percobaan} percobaan.")
            break

    except ValueError:
        print("Masukkan angka yang valid!\n")