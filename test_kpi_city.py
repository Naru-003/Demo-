import pytest
from src.kpi_city import city_kpi

def test_city_kpi_happy_path():
    # Average for Mumbai is (50.5 + 120.0 + 30.0) / 3 = 66.833
    result = city_kpi("Mumbai")
    assert result is not None
    assert 66.8 < result < 66.9

def test_city_kpi_injection_safety():
    # A secure query should return None for an injection string, not all rows
    result = city_kpi("Mumbai' OR 1=1 --")
    assert result is None