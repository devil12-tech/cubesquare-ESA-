from cubesquare import cubesquare_details


def test_cubesquare_details():
    expected_output = {
        "num": 2,
        "square": 4,
        "cube": 8
    }
    assert cubesquare_details(2) == expected_output

    expected_output = {
        "num": 3,
        "square": 9,
        "cube": 27
    }
    assert cubesquare_details(3) == expected_output

    expected_output = {
        "num": 4,
        "square": 16,
        "cube": 64
    }
    assert cubesquare_details(4) == expected_output
