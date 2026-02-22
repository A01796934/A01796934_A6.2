"""
Unit tests for the Customer class.
"""
import unittest
import os
from src.customer import Customer


class TestCustomer(unittest.TestCase):
    """Test cases for Customer class."""

    def setUp(self):
        """Cleanup before tests."""
        self.path = "data/customers.json"
        if os.path.exists(self.path):
            os.remove(self.path)

    def test_display_existing_customer(self):
        """Test displaying an existing customer."""
        cust = Customer(201, "Alice", "alice@test.com")
        cust.save_to_file()
        result = Customer.display_customer(201)
        self.assertEqual(result['name'], "Alice")

    def test_modify_customer_name(self):
        """Test modifying customer information."""
        cust = Customer(202, "Bob", "bob@test.com")
        cust.save_to_file()
        success = Customer.modify_customer(202, "Robert")
        self.assertTrue(success)
        # Verificar que se guardó el cambio
        updated = Customer.display_customer(202)
        self.assertEqual(updated['name'], "Robert")

    def test_modify_non_existent(self):
        """Negative test: Modify ID that does not exist."""
        result = Customer.modify_customer(999, "No One")
        self.assertFalse(result)
