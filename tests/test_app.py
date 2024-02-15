# test_main.py
from app import App

def test_app():
    # Call the create method to get an instance of App
    app = App.create()

    # Check if `app` is an instance of `App`
    assert isinstance(app, App)
