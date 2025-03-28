from gendiff.scripts.gendiff import generate_diff


def test_generate_diff_json():
    file1 = "tests/test_data/file1_test.json"
    file2 = "tests/test_data/file2_test.json"
    
    expected = (
        "{\n"
        "    - follow: false\n"
        "      host: hexlet.io\n"
        "    - proxy: 123.234.53.22\n"
        "    - timeout: 50\n"
        "    + timeout: 20\n"
        "    + verbose: true\n"
        "}"
    )
    
    result = generate_diff(file1, file2)
    assert result == expected


def test_generate_diff_yml():
    file1 = "tests/test_data/file1_test.yml"
    file2 = "tests/test_data/file2_test.yml"
    
    expected = (
        "{\n"
        "    - follow: false\n"
        "      host: hexlet.io\n"
        "    - proxy: 123.234.53.22\n"
        "    - timeout: 50\n"
        "    + timeout: 20\n"
        "    + verbose: true\n"
        "}"
    )

    result = generate_diff(file1, file2)
    assert result == expected
