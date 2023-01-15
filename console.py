#!/usr/bin/python3
"""Defines the HBNB console."""
import cmd
from shlex import split
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class Place:
    """A class representing a place to stay."""

    def __init__(self, name, city, owner, price):
        """Initialize a Place instance.

        Args:
            name (str): The name of the place.
            city (str): The city where the place is located.
            owner (str): The owner of the place.
            price (float): The nightly rental price of the place.
        """
        self.name = name
        self.city = city
        self.owner = owner
        self.price = price
        self.guests = []

    def __str__(self):
        """Return a string representation of the Place instance."""
        return f"{self.name} in {self.city}, owned by {self.owner}."

    def add_guest(self, guest_name):
        """Add a guest to the list of guests staying at the place.

        Args:
            guest_name (str): The name of the guest.
        """
        self.guests.append(guest_name)

    def remove_guest(self, guest_name):
        """Remove a guest from the list of guests staying at the place.

        Args:
            guest_name (str): The name of the guest.
        """
        self.guests.remove(guest_name)

    def available(self):
        """Check if the place is available for rent.

        Returns:
            bool: True if the place is available, False otherwise.
        """
        return not self.guests

