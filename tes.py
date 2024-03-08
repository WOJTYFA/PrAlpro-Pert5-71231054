def perkalian(a, b):
    hasil = 0
    for _ in range(b):
        hasil += a
    return hasil

def main():
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))

    hasil_perkalian = perkalian(angka1, angka2)
    print(f"{angka1} x {angka2} = {' + '.join(str(angka1) for _ in range(angka2))} = {hasil_perkalian}")

if __name__ == "__main__":
    main()
