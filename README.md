# CareerUp

**Repo:** `CareerUp_UAS_SDF` — UAS Software Development Fundamentals, Kelompok 1.

CareerUp adalah platform simulasi pekerjaan untuk pencari kerja dan fresh graduate yang belum yakin apakah dirinya siap untuk suatu pekerjaan. Job Seeker memilih pekerjaan target, mempelajari skill yang dibutuhkan lewat materi singkat, lalu mengerjakan tugas simulasi yang meniru pekerjaan aslinya. Setelah itu sistem memberi skor, status kesiapan (Siap, Hampir Siap, atau Perlu Latihan Lagi), dan saran materi yang perlu diulang, sehingga pengguna tahu posisinya sebelum melamar kerja sungguhan.

## Anggota Tim

| Nama | NIM | GitHub |
|---|---|---|
| Abdullah Azzam Firdaus | 26110300018 | @AZZAMAF |
| Azkiya Raihana | 26110300008  | @rockiny4n |
| Sahfria Elisabeth Yaleget | 26110300019 | @yalegetsahfria092-debug |

## Deliverable

| Deliverable | Dokumen |
|---|---|
| D1. Topic & Problem Statement | [docs/D1.md](docs/D1.md) |
| D2. Module Breakdown | [docs/D2.md](docs/D2.md) |
| D3. Use Case Diagram | [diagrams/usecase.puml](diagrams/usecase.puml) |
| D4. Sequence Diagram | [docs/D4.md](docs/D4.md) |
| D6. Test Case (skenario simulasi S2) | [docs/D6.md](docs/D6.md) |
| D7. Fungsi `evaluate_simulation` + unit test | [docs/D7.md](docs/D7.md) |
| Pembagian tugas tim | [docs/PEMBAGIAN_TUGAS.md](docs/PEMBAGIAN_TUGAS.md) |
| Activity log | [ACTIVITY_LOG.md](ACTIVITY_LOG.md) |

## Cara menjalankan test

```bash
pip install -r requirements.txt
pytest
```

## Penggunaan AI

- Tool: Hermes Agent (Nous Research)
- Digunakan untuk: menyusun teks D1-D7, generate kode D7 dan unit test, membuat sequence diagram PlantUML, review konsistensi terminologi antar dokumen
- Bagian yang direvisi tim: D1 (konsistensi aktor), D2 (konsistensi aktor), D4 (penyesuaian skenario dengan spec baru), D6 (penyesuaian test case dengan aturan bisnis D7), D7 (kode dan test), pembagian tugas (penyesuaian pemegang diagram)
