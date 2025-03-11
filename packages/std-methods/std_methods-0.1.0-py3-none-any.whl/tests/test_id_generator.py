# tests/test_id_generator.py
from common_library.utils.id_generator import generate_id


def test_generate_id():
    id_value = generate_id("Test")
    assert id_value.startswith("Test-")
