# Pertemuan 13 - Debugging dan Testing

**Nama:** Rijal Munawarudin
**NIM:** 2225250151
**Kelas:** 3F

## Kasus

Praktik ini membahas investigasi dan perbaikan bug pada program Python, khususnya kesalahan perhitungan rata-rata, penentuan status kelulusan, dan pencarian nilai tertinggi.

## Test Case

| ID | Input              | Expected           | Actual Awal | Status |
| -- | ------------------ | ------------------ | ----------- | ------ |
| T1 | `[80, 60, 90, 70]` | Rata-rata 75.0     | 60.0        | FAIL   |
| T2 | `[100, 80]`        | Rata-rata 90.0     | 36.0        | FAIL   |
| T3 | `60`               | Lulus              | Tidak lulus | FAIL   |
| T4 | `59`               | Tidak lulus        | Tidak lulus | PASS   |
| T5 | `[80, 60, 90, 70]` | Nilai tertinggi 90 | 0           | FAIL   |

## Bug Report

**B01 - Bug rata-rata**

* Gejala: hasil rata-rata tidak sesuai.
* Lokasi: fungsi `hitung_rata_rata()`.
* Akar penyebab: program menggunakan pembagi tetap 5.
* Perbaikan: membagi jumlah nilai dengan `len(nilai)`.

**B02 - Bug status kelulusan**

* Gejala: nilai 60 dinyatakan tidak lulus.
* Lokasi: fungsi `status()`.
* Akar penyebab: menggunakan operator `>` sehingga nilai 60 tidak memenuhi kondisi.
* Perbaikan: mengganti operator menjadi `>=`.

**B03 - Bug nilai tertinggi**

* Gejala: nilai tertinggi menghasilkan 0.
* Lokasi: fungsi `nilai_tertinggi()`.
* Akar penyebab: kondisi perbandingan menggunakan operator `<`.
* Perbaikan: menggunakan operator `>` dan memulai nilai tertinggi dari elemen pertama.

## Retest

| ID | Expected    | Actual Setelah Perbaikan | Status |
| -- | ----------- | ------------------------ | ------ |
| T1 | 75.0        | 75.0                     | PASS   |
| T2 | 90.0        | 90.0                     | PASS   |
| T3 | Lulus       | Lulus                    | PASS   |
| T4 | Tidak lulus | Tidak lulus              | PASS   |
| T5 | 90          | 90                       | PASS   |

## Cara Menjalankan

Jalankan perintah berikut dari folder utama proyek:

```bash
python praktik/praktik_4_debugging.py
```

Jika perintah `python` tidak tersedia, gunakan `python3`.

## Refleksi

Teknik debugging yang paling membantu adalah tracing dan testing menggunakan test case. Tracing membantu mengetahui perubahan nilai variabel, sedangkan test case membantu membandingkan hasil yang diharapkan dengan hasil aktual. Setelah bug diperbaiki, seluruh test case perlu dijalankan kembali untuk memastikan perbaikan berhasil dan tidak menimbulkan kesalahan baru.
