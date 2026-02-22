"""
Unit tests for the Hotel class.
"""
import unittest
import os
import json
from src.hotel import Hotel


class TestHotel(unittest.TestCase):
    """Test cases for Hotel class persistence and error handling."""

    def setUp(self):
        """Prepare environment before each test."""
        self.data_path = "data/hotels.json"
        if not os.path.exists("data"):
            os.makedirs("data")
        if os.path.exists(self.data_path):
            os.remove(self.data_path)

    def test_create_hotel_positive(self):
        """Positive test: Verify hotel is saved correctly."""
        hotel = Hotel(1, "Grand Hotel", "Mexico City", 100)
        hotel.save_to_file()
        self.assertTrue(os.path.exists(self.data_path))

    def test_to_dict(self):
        """Positive test: Verify dictionary conversion."""
        hotel = Hotel(2, "Plaza", "Monterrey", 50)
        expected = {
            "hotel_id": 2,
            "name": "Plaza",
            "location": "Monterrey",
            "rooms": 50
        }
        self.assertEqual(hotel.to_dict(), expected)

    # CASOS NEGATIVOS (Requeridos para puntaje máximo)
    def test_delete_non_existent_hotel(self):
        """Negative 1: Attempt to delete a hotel that doesn't exist."""
        hotel = Hotel(1, "Existent", "City", 10)
        hotel.save_to_file()
        result = Hotel.delete_hotel(999)
        # Cambiar a assertFalse porque el hotel 999 no existe
        self.assertFalse(result)        

    def test_load_corrupt_json(self):
        """Negative 2: Handle a corrupted JSON file during save."""
        with open(self.data_path, 'w', encoding='utf-8') as file:
            file.write("not a json content")
        hotel = Hotel(3, "Faulty", "City", 10)
        hotel.save_to_file()  # Debe manejar el error internamente
        self.assertTrue(os.path.exists(self.data_path))

    def test_delete_missing_file(self):
        """Negative 3: Attempt to delete when file does not exist."""
        if os.path.exists(self.data_path):
            os.remove(self.data_path)
        result = Hotel.delete_hotel(1)
        self.assertFalse(result)

    def test_invalid_data_structure(self):
        """Negative 4: Handle file with invalid list structure."""
        with open(self.data_path, 'w', encoding='utf-8') as file:
            file.write("[]") 
        result = Hotel.delete_hotel(1)
        # No debería fallar el programa
        self.assertFalse(result)

    def test_save_to_readonly_directory(self):
        """Negative 5: Save error handling with invalid path."""
        hotel = Hotel(4, "Error", "None", 0)
        # Usamos una ruta que claramente no existe o es restringida
        hotel.file_path = "/proc/invalid_path.json" 
        hotel.save_to_file() 
        # El test pasa si no lanza excepción (el error se atrapa en src)
        self.assertFalse(os.path.exists(hotel.file_path))       

if __name__ == '__main__':
    unittest.main()
