import unittest
from services.console_service import ConsoleService

import unittest
from services.console_service import ConsoleService

class FakeConsoleRepository:
    def __init__(self):
        self.consoles = [
            {"id": 1, "name": "PlayStation"},
            {"id": 2, "name": "Xbox"},
        ]

    def get_all_consoles(self):
        return list(self.consoles)

    def get_console_by_id(self, console_id):
        for console in self.consoles:
            if console["id"] == console_id:
                return console
        return None

    def get_console_by_name(self, name):
        for console in self.consoles:
            if console["name"].lower() == name.lower():
                return console
        return None

class TestConsoleService(unittest.TestCase):
    def setUp(self):
        self.repo = FakeConsoleRepository()
        self.service = ConsoleService(self.repo)

    def test_get_all_consoles(self):
        consoles = self.service.get_all_consoles()
        self.assertEqual(len(consoles), 2)

    def test_get_console_by_id(self):
        console = self.service.get_console_by_id(1)
        self.assertEqual(console["name"], "PlayStation")

    def test_get_console_by_name(self):
        console = self.service.get_console_by_name("Xbox")
        self.assertEqual(console["id"], 2)

    def test_get_console_by_id_not_found(self):
        console = self.service.get_console_by_id(100)
        self.assertIsNone(console)

    def test_get_console_by_name_not_found(self):
        console = self.service.get_console_by_name("Test")
        self.assertIsNone(console)
