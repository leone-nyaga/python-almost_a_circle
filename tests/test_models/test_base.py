import unittest
import os
from models.base import Base

class TestBase(unittest.TestCase):
    
    def test_constructor_with_id(self):
        """Test constructor with a given id."""
        obj = Base(5)
        self.assertEqual(obj.id, 5)

    def test_constructor_without_id(self):
        """Test constructor without id generates a new id."""
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_to_json_string_with_valid_input(self):
        """Test to_json_string with valid input."""
        dicts = [{"id": 1, "width": 2, "height": 3}]
        json_str = Base.to_json_string(dicts)
        self.assertEqual(json_str, '[{"id": 1, "width": 2, "height": 3}]')

    def test_to_json_string_with_empty_input(self):
        """Test to_json_string with an empty list."""
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_to_json_string_with_none_input(self):
        """Test to_json_string with None."""
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")

    def test_save_to_file(self):
        """Test save_to_file writes to file correctly."""
        obj = Base(1)
        filename = "Base.json"
        
        # Clean up the file if it exists
        if os.path.exists(filename):
            os.remove(filename)
        
        Base.save_to_file([obj])
        
        # Check if file exists
        self.assertTrue(os.path.exists(filename))

        with open(filename, 'r') as file:
            content = file.read()
            expected_content = Base.to_json_string([{"id": 1}])
            self.assertEqual(content, expected_content)

        # Clean up after test
        os.remove(filename)

if __name__ == '__main__':
    unittest.main()

