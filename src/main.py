import json

import yaml


class HelloWorld:
    """Hello world class"""

    def __init__(self, name: str) -> None:
        self.name = name
        self.config = yaml.safe_load("example.yaml")

        self.json_data = {"key": "value"}
        self.dump = json.dumps(self.json_data)

    def greeting(self) -> str:
        """Greeting function"""
        return f"Hello {self.name}!"

    def Goodbye(self) -> str:
        """Goodbye function"""
        return "Goodbye!"
