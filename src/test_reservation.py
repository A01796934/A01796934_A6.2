"""
Unit tests for the Reservation class.
"""
import unittest
import os
from src.reservation import Reservation


class TestReservation(unittest.TestCase):
    """Test cases for Reservation class."""

    def setUp(self):
        """Cleanup data folder before tests."""
        self.path = "data/reservations.json"
        if os.path.exists(self.path):
            os.remove(self.path)

    def test_create_reservation(self):
        """Positive test for reservation creation."""
        res = Reservation(501, 101, 1)
        res.save_to_file()
        self.assertTrue(os.path.exists(self.path))

    def test_cancel_non_existent_reservation(self):
        """Negative test: Cancel ID that does not exist."""
        result = Reservation.cancel_reservation(999)
        self.assertFalse(result)

    def test_cancel_with_corrupt_file(self):
        """Negative test: Handle invalid JSON."""
        with open(self.path, 'w', encoding='utf-8') as f:
            f.write("invalid")
        result = Reservation.cancel_reservation(501)
        self.assertFalse(result)
