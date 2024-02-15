"""Hello World of App Example Test File"""
from app import App

def test_app():
    """Creation of an App Instance"""
    app = App.create()

    # Check if `app` is an instance of `App`
    assert isinstance(app, App)
