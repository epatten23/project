from weather import convert_temp, convert_distance, convert_pressure, convert_speed
import pytest

def test_convert_temp():
    assert convert_temp(240) == -28
    assert convert_temp(271.45) == 29
    assert convert_temp(305) == 89

def test_convert_distance():
    assert convert_distance(13000) == 13
    assert convert_distance(3000) == 3
    assert convert_distance(25500) == 25.5

def test_convert_pressure():
    assert convert_pressure(100)  == 1.45038
    assert convert_pressure(50)   == 0.72519
    assert convert_pressure(1000) == 14.5038

def test_convert_speed():
    assert convert_speed(1) == 2.24
    assert convert_speed(25) == 55.93
    assert convert_speed(13.5) == 30.20


pytest.main(["-v", "--tb=line", "-rN", __file__])