"""
Module for Managing Customer Information
"""
import json
import os


class Customer:
    """
    Class to represent a Customer and its persistent operations.
    """
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.file_path = "data/customers.json"

    def to_dict(self):
        """Convert customer object to dictionary."""
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email
        }

    def save_to_file(self):
        """Save the customer data to a JSON file."""
        customers = []
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r', encoding='utf-8') as file:
                    customers = json.load(file)
            except (json.JSONDecodeError, FileNotFoundError):
                print("Error loading customer file. Starting new.")
        customers.append(self.to_dict())
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(customers, file, indent=4)

    @staticmethod
    def delete_customer(customer_id):
        """Delete a customer by ID from the file."""
        file_path = "data/customers.json"
        if not os.path.exists(file_path):
            return False
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                customers = json.load(file)
            filtered = [
                c for c in customers if c['customer_id'] != customer_id
            ]
            if len(filtered) == len(customers):
                return False
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(filtered, file, indent=4)
            return True
        except (json.JSONDecodeError, FileNotFoundError):
            return False
