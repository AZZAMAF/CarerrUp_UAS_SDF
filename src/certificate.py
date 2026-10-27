"""CareerUp - evaluasi hasil simulasi pekerjaan."""

def evaluate_simulation(correct: int, total: int) -> str:
    """Hitung status kesiapan berdasarkan jumlah jawaban benar dan total task.

    Aturan:
    - Siap: persentase >= 80
    - Hampir Siap: persentase >= 60 dan < 80
    - Perlu Latihan Lagi: persentase < 60

    Raises:
        ValueError: jika total <= 0 atau correct di luar rentang [0, total].
    """
    if total <= 0:
        raise ValueError("Total task harus lebih dari 0")
    if correct < 0 or correct > total:
        raise ValueError("Jumlah jawaban benar tidak valid")

    percentage = (correct / total) * 100

    if percentage >= 80:
        return "Siap"
    if percentage >= 60:
        return "Hampir Siap"
    return "Perlu Latihan Lagi"
