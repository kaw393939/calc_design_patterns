"""Hello World of App Example Test File"""
from app import App

def test_app_start(capfd):
    """Hello World Prints When Main starts"""

    App.start()
    out, err = capfd.readouterr() # pylint: disable=unused-variable
    assert out == "Hello World\n"
