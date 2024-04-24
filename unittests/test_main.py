import unittest
from include_json.main import read_json

class TestReadJson(unittest.TestCase):

    def test_read_json_data_not_empty(self):
        data = read_json()
        self.assertIsNotNone(data)
        self.assertTrue(data)

    def test_read_json_name_is_John_Doe(self):
        data = read_json()
        self.assertEqual(data.get('name'), "John Doe")

    def test_read_json_has_phone_numbers_key(self):
        data = read_json()
        self.assertTrue('phone_numbers' in data)

    def test_read_json_has_address_key(self):
        data = read_json()
        self.assertTrue('address' in data)

if __name__ == '__main__':
    unittest.main()
