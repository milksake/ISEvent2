from flask import Flask
from app import create_app
import os

config_class= "config.Config"
app = create_app(config_class)

if __name__ == "__main__":
    app.run(debug=True)
