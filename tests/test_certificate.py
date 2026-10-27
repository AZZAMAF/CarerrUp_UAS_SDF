"""Unit test untuk fungsi evaluate_simulation (D7)."""

import pytest
from src.certificate import evaluate_simulation


class TestEvaluateSimulation:
    """TC berdasarkan D6."""

    def test_tc01_semua_benar(self):
        assert evaluate_simulation(10, 10) == "Siap"

    def test_tc02_sebagian_benar(self):
        assert evaluate_simulation(7, 10) == "Hampir Siap"

    def test_tc03_banyak_salah(self):
        assert evaluate_simulation(3, 10) == "Perlu Latihan Lagi"

    def test_tc07_batas_bawah_siap(self):
        assert evaluate_simulation(8, 10) == "Siap"

    def test_tc08_tepat_di_bawah_siap(self):
        assert evaluate_simulation(79, 100) == "Hampir Siap"

    def test_tc09_batas_bawah_hampir_siap(self):
        assert evaluate_simulation(6, 10) == "Hampir Siap"

    def test_tc10_tidak_ada_benar(self):
        assert evaluate_simulation(0, 10) == "Perlu Latihan Lagi"

    def test_tc12_total_nol_error(self):
        with pytest.raises(ValueError):
            evaluate_simulation(0, 0)

    def test_tc13_correct_negatif_error(self):
        with pytest.raises(ValueError):
            evaluate_simulation(-1, 10)

    def test_tc13_correct_melebihi_total_error(self):
        with pytest.raises(ValueError):
            evaluate_simulation(11, 10)
