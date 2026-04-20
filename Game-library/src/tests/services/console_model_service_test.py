import unittest
from services.console_model_service import ConsoleModelService

class FakeConsoleModelRepository:
    def __init__(self):
        self.models = [
            {"id": 1, "name": "PS5"},
            {"id": 2, "name": "Xbox 360"},
            {"id": 3, "name": "Nintendo Switch"}
        ]

    def get_all_console_models(self):
        return list(self.models)

    def get_console_model_by_id(self, model_id):
        for model in self.models:
            if model["id"] == model_id:
                return model
        return None

    def get_console_model_by_name(self, name):
        for model in self.models:
            if model["name"].lower() == name.lower():
                return model
        return None

class TestConsoleModelService(unittest.TestCase):
    def setUp(self):
        self.repo = FakeConsoleModelRepository()
        self.service = ConsoleModelService(self.repo)

    def test_fetch_all_models(self):
        models = self.service.fetch_all_models()
        self.assertEqual(len(models), 3)

    def test_get_model_by_id(self):
        model = self.service.get_model_by_id(1)
        self.assertEqual(model["name"], "PS5")

    def test_get_model_by_name(self):
        model = self.service.get_model_by_name("Xbox 360")
        self.assertEqual(model["id"], 2)
