"""
Module for Managing Reservations
"""
import json
import os


class Reservation:
    """
    Class to represent a Reservation between a Customer and a Hotel.
    """
    def __init__(self, reservation_id, customer_id, hotel_id):
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id
        self.file_path = "data/reservations.json"

    def to_dict(self):
        """Convert reservation object to dictionary."""
        return {
            "reservation_id": self.reservation_id,
            "customer_id": self.customer_id,
            "hotel_id": self.hotel_id
        }

    def save_to_file(self):
        """Save the reservation data to a JSON file."""
        reservations = []
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r', encoding='utf-8') as file:
                    reservations = json.load(file)
            except (json.JSONDecodeError, FileNotFoundError):
                print("Error loading reservations. Starting new.")
        reservations.append(self.to_dict())
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(reservations, file, indent=4)

    @staticmethod
    def cancel_reservation(reservation_id):
        """Cancel a reservation by ID from the file."""
        file_path = "data/reservations.json"
        if not os.path.exists(file_path):
            return False
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reservations = json.load(file)
            filtered = [
                r for r in reservations
                if r['reservation_id'] != reservation_id
            ]
            if len(filtered) == len(reservations):
                return False
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(filtered, file, indent=4)
            return True
        except (json.JSONDecodeError, FileNotFoundError):
            return False
