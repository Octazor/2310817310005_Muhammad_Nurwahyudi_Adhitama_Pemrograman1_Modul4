while True:
    print("Pilih program:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Exit")
    
    pilihan = int(input("Masukkan Pilihan: "))

    if pilihan == 5:
        print("Terimakasih, telah menggunakan kalkulator Muhammad Nurwahyudi Adhitama")
        break

    if pilihan < 1 or pilihan > 4:
        print("Input anda salah, Silakan coba lagi.")
        continue

    nilaiPertama = float(input("Masukkan nilai pertama: "))
    nilaiKedua = float(input("Masukkan nilai kedua: "))

    if pilihan == 1:
        print(f"Hasil Penjumlahan antara {nilaiPertama:.2f} dan {nilaiKedua:.2f} adalah {nilaiPertama + nilaiKedua:.2f}")
    elif pilihan == 2:
        print(f"Hasil Pengurangan antara {nilaiPertama:.2f} dan {nilaiKedua:.2f} adalah {nilaiPertama - nilaiKedua:.2f}")
    elif pilihan == 3:
        print(f"Hasil Perkalian antara {nilaiPertama:.2f} dan {nilaiKedua:.2f} adalah {nilaiPertama * nilaiKedua:.2f}")
    elif pilihan == 4:
        if nilaiKedua != 0:
            print(f"Hasil Pembagian antara {nilaiPertama:.2f} dan {nilaiKedua:.2f} adalah {nilaiPertama / nilaiKedua:.2f}")
        else:
            print("Pembagian oleh nol tidak valid.")
