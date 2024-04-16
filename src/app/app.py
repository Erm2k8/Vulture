from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

def show_configs() -> None:
    for key, value in app.config.items():
        print(f"{key}: {value}")