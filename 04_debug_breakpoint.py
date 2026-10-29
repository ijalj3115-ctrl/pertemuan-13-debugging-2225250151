def hitung_rata_rata(data):
    if len(data) == 0:
        return 0

    total = sum(data)
    rata = total / len(data)
    return rata


nilai = [80, 90, 70]

hasil = hitung_rata_rata(nilai)
print("Rata-rata:", hasil)