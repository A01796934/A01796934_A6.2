"""
Module for Managing Hotel Information
"""
import json
import os


class Hotel:
    """
    Class to represent a Hotel and its persistent operations.
    """
    def __init__(self, hotel_id, name, location, rooms):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.rooms = rooms
        self.file_path = "data/hotels.json"

    def to_dict(self):
        """Convert hotel object to dictionary."""
        return {
            "hotel_id": self.hotel_id,
            "name": self.name,
            "location": self.location,
            "rooms": self.rooms
        }

    def save_to_file(self):
        """Save the hotel data to a JSON file."""
        hotels = []
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r', encoding='utf-8') as file:
                    hotels = json.load(file)
            except (json.JSONDecodeError, FileNotFoundError) as error:
                print(f"Error loading file: {error}. Starting new.")

        hotels.append(self.to_dict())
        try:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump(hotels, file, indent=4)
        except (PermissionError, FileNotFoundError) as error:
            print(f"Error saving to file: {error}")

    @staticmethod
    def delete_hotel(hotel_id):
        """Delete a hotel by ID from the file."""
        file_path = "data/hotels.json"
        if not os.path.exists(file_path):
            return False
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                hotels = json.load(file)
            # Verificar si el ID existe antes de filtrar
            if not any(h.get('hotel_id') == hotel_id for h in hotels):
                return False

            remaining = [h for h in hotels if h.get('hotel_id') != hotel_id]
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(remaining, file, indent=4)
            return True
        except (json.JSONDecodeError, KeyError):
            print("Error: Invalid data format in file.")
            return False
