from gendiff.scripts.gendiff import generate_diff


def read_file(path):
    with open(path) as f:
        return f.read().strip()


def test_generate_diff_json():
    file1 = "tests/test_data/file1_test.json"
    file2 = "tests/test_data/file2_test.json"
    expected = read_file("tests/test_data/expected_stylish.txt")
    result = generate_diff(file1, file2)
    assert result == expected


def test_generate_diff_yml():
    file1 = "tests/test_data/file1_test.yml"
    file2 = "tests/test_data/file2_test.yml"
    expected = read_file("tests/test_data/expected_stylish.txt")
    result = generate_diff(file1, file2)
    assert result == expected
