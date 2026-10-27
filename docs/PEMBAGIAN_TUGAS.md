# Pembagian Tugas Tim CareerUp

**Kelompok 1** | UAS Software Development Fundamentals
**Deadline:** Kamis, 29 Oktober 2026, 10:00 WIB (target selesai internal: **Rabu, 28 Oktober malam**)

## Anggota

| Nama | GitHub | Peran utama |
|---|---|---|
| Abdullah Azzam Firdaus (ketua) | @AZZAMAF | D1, sequence diagram 3, README, reviewer |
| Azkiya Raihana | @rockiny4n | D2, D3, sequence diagram 1, D6 common |
| Sahfria Elisabeth Yaleget | @yalegetsahfria092-debug | Sequence diagram 2, D6 edge case, D7 |

## Ringkasan Pembagian Deliverable

| Deliverable | Penanggung jawab | Reviewer |
|---|---|---|
| D1. Topik & Masalah | Azzam | Azkiya |
| D2. Modul | Azkiya | Azzam |
| D3. Use Case Diagram | Azkiya | Azzam |
| D4. Sequence Diagram 1: Job Seeker menetapkan pekerjaan target dan roadmap | Azkiya | Sahfria |
| D4. Sequence Diagram 2: Sistem mengevaluasi simulasi | Sahfria | Azzam |
| D4. Sequence Diagram 3: Job Seeker mengulang simulasi (jalan B) | Azzam | Azkiya |
| D6. Test Case (skenario simulasi S2) | Sahfria  | Azzam |
| D7. Fungsi `evaluate_simulation` + unit test | Sahfria | Azkiya |
| README.md | Azzam | Azkiya, Sahfria |
| ACTIVITY_LOG.md | Masing-masing mengisi entri sendiri | - |

**Catatan penting:** nama aktor harus sama di semua dokumen.

## Detail Tugas per Orang

### Azzam
1. Tulis D1 (`docs/D1.md`) dan buat commit.
2. Gambar sequence diagram 3 (mengulang simulasi, jalan B, ada alur `alt`: ulang lagi vs selesai).
3. Tulis dan rapikan README (link deliverable, cara run test, penggunaan AI, anggota tim).
4. Review PR Azkiya dan Sahfria.
5. Isi activity log sendiri setiap selesai kerja.

### Azkiya
1. Tulis D2 (`docs/D2.md`) dari konsep modul CareerUp yang baru, lalu buat branch dan PR.
2. Tulis use case diagram (PlantUML + export `.png`), commit sebagai D3.
3. Gambar sequence diagram 1 (menetapkan pekerjaan target dan roadmap, `alt`: roadmap berhasil vs perlu revisi).
4. Tulis 5 test case common untuk skenario simulasi S2 di D6.
5. Review PR Sahfria dan Azzam dengan komentar singkat.
6. Isi activity log sendiri setiap selesai kerja.

### Sahfria
1. Gambar sequence diagram 2 (evaluasi simulasi, ada alur `alt`: hasil lolos vs gagal).
2. Tulis 5 edge case di D6 berdasarkan kategori dari spec.
3. Kode D7 (`evaluate_simulation`) + unit test di `tests/test_certificate.py` (atau file baru kalau namanya berubah), lalu buat PR.
4. Review PR Azkiya dan Azzam dengan komentar singkat.
5. Isi activity log sendiri setiap selesai kerja.

## Rencana Commit (min. 3 commit bermakna per orang)

| Orang | Commit 1 | Commit 2 | Commit 3 | Commit 4 |
|---|---|---|---|---|
| Azzam | Tambah D1 | Tambah sequence diagram 3 | Tambah README | Review PR |
| Azkiya | Tambah D2 | Tambah use case diagram (`.puml` + `.png`) | Tambah sequence diagram 1 | Tambah 5 test case common D6 |
| Sahfria | Tambah sequence diagram 2 | Tambah 5 edge case D6 | Tambah kode D7 + unit test | Review PR |

Commit untuk activity log boleh ditambah, tapi **bukan pengganti** commit di atas.

## Rencana Pull Request (min. 2, masing-masing di-review anggota lain)

| PR | Isi | Dibuat oleh | Reviewer |
|---|---|---|---|
| PR #1 | D2 + D3 Use Case Diagram | Azkiya | Azzam + Sahfria |
| PR #2 | Sequence Diagram 2 + D6 edge case + D7 | Sahfria | Azzam + Azkiya |
| PR #3 (opsional) | Sequence Diagram 1 + D6 common | Azkiya | Sahfria + Azzam |
| PR #4 (opsional) | D1 + README | Azzam | Azkiya + Sahfria |

Aturan: **tidak ada yang merge PR miliknya sendiri sebelum direview** minimal 1 orang.

## Jadwal

| Tanggal | Target |
|---|---|
| Selasa 27 Okt | D1, D2, D3 di-commit, PR #1 dibuka, ketiga sequence diagram digambar |
| Rabu 28 Okt | D6, D7, README, dan activity log selesai |
| Kamis 29 Okt | Cek akhir dan **submit sebelum 10:00** |

## Aturan Tim

1. **Jangan commit langsung ke `main`.** Selalu pakai branch lalu Pull Request.
2. Nama branch: `d<nomor>-<nama>`, contoh `d3-azkiya`.
3. Pesan commit jelas, contoh: `Add sequence diagram 3 for retry simulation`. Jangan `update` atau `fix` saja.
4. Atur `git config user.name` dan `user.email` dengan email yang terhubung ke akun GitHub masing-masing, supaya commit tampil atas nama sendiri.
5. Activity log (`ACTIVITY_LOG.md`) diisi **sendiri** dari akun GitHub masing-masing, **setiap selesai kerja**, dengan hash commit atau nomor PR sebagai bukti. Jangan menulis atas nama teman.
6. Tanggal di activity log harus sesuai tanggal kerja sebenarnya.
7. Semua anggota harus bisa menjelaskan **bagian mana pun** dari proyek jika ditanya dosen.
8. Jika memakai AI, catat di README alat apa dan untuk apa.
9. Jika memakai PlantUML, simpan source `.puml` dan export `.png`/`.svg` ke folder `diagrams/`.

## Checklist Akhir

- [ ] D1 sampai D7 ada dan ter-link di README
- [ ] Diagram punya gambar (`.png`/`.svg`) **dan** file source
- [ ] Tiap anggota punya minimal 3 commit bermakna
- [ ] Minimal 2 PR yang direview anggota lain
- [ ] Tiap anggota memegang 1 sequence diagram
- [ ] Nama aktor konsisten di semua dokumen
- [ ] Activity log lengkap dan cocok dengan riwayat commit
- [ ] README: nama app, anggota (nama + NIM + username GitHub), link deliverable, cara run test, bagian penggunaan AI
- [ ] Screenshot test lulus
- [ ] Repo publik (atau dosen sudah ditambahkan sebagai collaborator)
- [ ] Link repo disubmit sebelum Kamis 29 Okt, 10:00 WIB
