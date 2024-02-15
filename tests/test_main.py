"""Hello World of Main Example Test File"""
from main import main

def test_hello_world(capfd):
    """Hello World Prints When Main starts"""

    main()  # Call the main function directly
    out, err = capfd.readouterr() # pylint: disable=unused-variable
    assert out == "Hello World\n"
    