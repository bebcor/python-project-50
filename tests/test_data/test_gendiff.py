from gendiff.scripts.gendiff import generate_diff


def test_generate_diff():
    file1 = "tests/test_data/file1_test.json"
    file2 = "tests/test_data/file2_test.json"
    
    expected = """{
  - "follow": false,
    "host": "hexlet.io",
  - "proxy": "123.234.53.22",
  - "timeout": 50,
  + "timeout": 20,
  + "verbose": true
}"""
    
    result = generate_diff(file1, file2)

    assert result == expected